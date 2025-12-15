import fs from 'node:fs/promises';
import path from 'node:path';
import { chromium } from 'playwright';
import TurndownService from 'turndown';
import { load as loadHtml } from 'cheerio';

const START_URL = 'https://cursor.com/docs/api';
const OUTPUT_MD_PATH = path.resolve('docs/api.md');
const OUTPUT_ENDPOINTS_JSON_PATH = path.resolve('docs/api-endpoints.json');
const GENERATED_NOTICE = [
  '## Licensing / attribution',
  '',
  'This repository is licensed as follows:',
  '',
  '- **Code**: GNU Affero General Public License v3.0 only (AGPL-3.0-only).',
  '- **Documentation and other non-code content**: Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0).',
  '',
  'This particular file is **generated** from public content at `https://cursor.com/docs/`.',
  'It may include or closely paraphrase third-party material; it is provided here for developer convenience.',
  'If you reuse generated output, ensure your usage complies with Cursor’s terms and any applicable copyright rules.',
].join('\\n');

function normalizeUrl(rawUrl) {
  try {
    const u = new URL(rawUrl);
    if (u.origin !== 'https://cursor.com') return null;
    u.hash = '';
    u.search = '';
    return u.toString();
  } catch {
    return null;
  }
}

function isDocsPage(url) {
  try {
    const u = new URL(url);
    return u.origin === 'https://cursor.com' && u.pathname.startsWith('/docs/');
  } catch {
    return false;
  }
}

function isApiDocsCandidate(url) {
  if (!isDocsPage(url)) return false;
  const { pathname } = new URL(url);

  // Cursor docs routes we care about:
  // - /docs/api (overview)
  // - /docs/**/api/** (API references)
  // - /docs/**/*-api (API reference pages)
  // - /docs/**/webhooks (API webhooks pages)
  if (pathname === '/docs/api') return true;
  if (pathname.includes('/api/')) return true;
  if (pathname.endsWith('/api')) return true;
  if (pathname.endsWith('-api')) return true;
  if (pathname.includes('-api/')) return true;
  if (pathname.includes('/webhooks')) return true;
  return false;
}

function uniq(arr) {
  return [...new Set(arr)];
}

function fixMethodSpacing(md) {
  // Some docs components render method badges adjacent to inline code, e.g. `GET` + `/v0/...`
  // can become `GET\`/v0/...\`` after HTML->MD conversion.
  return md
    .replace(/\b(GET|POST|PUT|PATCH|DELETE)(?=`)/g, '$1 ')
    .replace(/\b(GET|POST|PUT|PATCH|DELETE)(?=\/)/g, '$1 ');
}

function stripDocsUiNoise(md) {
  let out = md;

  // Cursor docs UI chrome that can end up in #main-content.
  out = out.replace(/^Copy page.*Explain more\s*$/gim, '');

  // Drop a leading breadcrumb "API" if it's immediately followed by a page heading.
  const lines = out.replace(/\r\n/g, '\n').split('\n');
  while (lines.length && lines[0].trim() === '') lines.shift();
  if (lines[0]?.trim() === 'API') {
    const nextNonEmpty = lines.slice(1).find((l) => l.trim() !== '');
    if (nextNonEmpty?.startsWith('# ')) lines.shift();
  }

  return lines.join('\n');
}

function compactEmptyLines(md) {
  return md
    .replace(/\r\n/g, '\n')
    .replace(/\n{3,}/g, '\n\n')
    .trim()
    .concat('\n');
}

function escapePipes(s) {
  return s.replace(/\|/g, '\\|');
}

async function extractPageContentAsMarkdown(page) {
  const html = await page.evaluate(() => {
    const el =
      document.querySelector('#main-content') || document.querySelector('article') || document.querySelector('main');
    return (el || document.body).innerHTML;
  });

  const $ = loadHtml(html);
  // Drop obvious layout elements if they got captured.
  $('nav, aside, footer, header').remove();

  const turndown = new TurndownService({
    codeBlockStyle: 'fenced',
    headingStyle: 'atx',
    hr: '---',
    bulletListMarker: '-',
  });

  // Keep tables as HTML (Turndown otherwise flattens them poorly).
  turndown.keep(['table', 'thead', 'tbody', 'tr', 'th', 'td']);

  const md = turndown.turndown($.root().html() ?? '');
  return compactEmptyLines(stripDocsUiNoise(fixMethodSpacing(md)));
}

async function extractEndpointPairs(page) {
  return await page.evaluate(() => {
    const root =
      document.querySelector('#main-content') ||
      document.querySelector('article') ||
      document.querySelector('main') ||
      document.body;
    const text = root?.innerText || '';

    // Some pages render METHOD and PATH on separate lines.
    const re = /(GET|POST|PUT|PATCH|DELETE)\s+(\/[^\s]+|https?:\/\/[^\s]+)/g;
    const pairs = [];

    let m;
    while ((m = re.exec(text))) {
      pairs.push({ method: m[1], path: m[2] });
    }

    return pairs;
  });
}

function normalizeEndpointPath(p) {
  try {
    const u = new URL(p);
    if (u.origin === 'https://api.cursor.com') return u.pathname;
  } catch {
    // not a URL
  }
  return p;
}

function isTemplateSegment(seg) {
  return seg.startsWith(':') || (seg.startsWith('{') && seg.endsWith('}'));
}

function isTemplatePath(p) {
  return p.split('/').some((seg) => isTemplateSegment(seg));
}

function templateMatchesConcrete(templatePath, concretePath) {
  const tSegs = templatePath.split('/').filter(Boolean);
  const cSegs = concretePath.split('/').filter(Boolean);
  if (tSegs.length !== cSegs.length) return false;
  for (let i = 0; i < tSegs.length; i++) {
    if (isTemplateSegment(tSegs[i])) continue;
    if (tSegs[i] !== cSegs[i]) return false;
  }
  return true;
}

function dropExampleConcreteEndpoints(endpoints) {
  // If the docs include both a parameterized route and a concrete example URL,
  // keep the parameterized route and drop the example.
  const byMethod = new Map();
  for (const e of endpoints) {
    const list = byMethod.get(e.method) || [];
    list.push(e);
    byMethod.set(e.method, list);
  }

  const out = [];
  for (const [method, list] of byMethod.entries()) {
    const templates = list.filter((e) => isTemplatePath(e.path)).map((e) => e.path);
    for (const e of list) {
      if (isTemplatePath(e.path)) {
        out.push(e);
        continue;
      }
      if (templates.some((t) => templateMatchesConcrete(t, e.path))) continue;
      out.push(e);
    }
  }
  return out;
}

async function extractCandidateUrlsFromDom(page) {
  return await page.evaluate(() => {
    const out = [];

    // Standard anchors
    for (const a of document.querySelectorAll('a[href]')) out.push(a.href);

    // Some Next.js docs UIs use data-href / data-to / role=link.
    for (const el of document.querySelectorAll('[data-href], [data-to], [data-url]')) {
      const v = el.getAttribute('data-href') || el.getAttribute('data-to') || el.getAttribute('data-url');
      if (!v) continue;
      try {
        out.push(new URL(v, window.location.href).toString());
      } catch {
        // ignore
      }
    }

    return out;
  });
}

async function main() {
  await fs.mkdir(path.dirname(OUTPUT_MD_PATH), { recursive: true });

  const browser = await chromium.launch();

  const queue = [START_URL];
  const visited = new Set();
  const pages = [];

  while (queue.length) {
    const next = queue.shift();
    const url = normalizeUrl(next);
    if (!url) continue;
    if (visited.has(url)) continue;
    if (!isApiDocsCandidate(url)) continue;

    visited.add(url);

    const page = await browser.newPage();
    const responseUrls = new Set();

    page.on('response', (resp) => {
      const u = normalizeUrl(resp.url());
      if (!u) return;
      // Next.js prefetch responses include ?_rsc=...; normalizeUrl strips them.
      if (isApiDocsCandidate(u)) responseUrls.add(u);
    });

    try {
      await page.goto(url, { waitUntil: 'networkidle', timeout: 60000 });
      // Give client-side nav/prefetch a moment.
      await page.waitForTimeout(1500);

      const title = await page.evaluate(() => {
        const h1 = document.querySelector('h1');
        return (h1?.textContent || document.title || '').trim();
      });

      const markdown = await extractPageContentAsMarkdown(page);
      const rawEndpoints = await extractEndpointPairs(page);
      const endpoints = dropExampleConcreteEndpoints(
        uniq(rawEndpoints.map((e) => `${e.method} ${normalizeEndpointPath(e.path)}`)).map((k) => {
          const firstSpace = k.indexOf(' ');
          return { method: k.slice(0, firstSpace), path: k.slice(firstSpace + 1) };
        }),
      );

      const domUrls = (await extractCandidateUrlsFromDom(page)).map(normalizeUrl).filter(Boolean);
      const discovered = uniq([...domUrls, ...responseUrls]);

      for (const d of discovered) {
        if (!visited.has(d) && isApiDocsCandidate(d)) queue.push(d);
      }

      pages.push({ url, title, endpoints, markdown });
    } finally {
      await page.close();
    }
  }

  await browser.close();

  // Build endpoint index.
  const endpointMap = new Map();
  for (const p of pages) {
    for (const e of p.endpoints) {
      const key = `${e.method} ${e.path}`;
      const existing = endpointMap.get(key) || { method: e.method, path: e.path, pages: new Set() };
      existing.pages.add(p.url);
      endpointMap.set(key, existing);
    }
  }

  const endpointIndex = [...endpointMap.values()]
    .map((v) => ({ method: v.method, path: v.path, pages: [...v.pages].sort() }))
    .sort((a, b) => (a.path === b.path ? a.method.localeCompare(b.method) : a.path.localeCompare(b.path)));

  const sortedPages = [...pages].sort((a, b) => (a.title || a.url).localeCompare(b.title || b.url));

  const lines = [];
  lines.push('# Cursor API (generated)');
  lines.push('');
  lines.push(`Source: ${START_URL}`);
  lines.push('');
  lines.push('This file is generated from the public Cursor docs and is intended to capture **all API endpoints, parameters, and response formats** present in those docs at generation time.');
  lines.push('');
  lines.push(GENERATED_NOTICE);
  lines.push('');
  lines.push('## Endpoint index');
  lines.push('');
  lines.push('| Method | Path | Documented in |');
  lines.push('| --- | --- | --- |');
  for (const e of endpointIndex) {
    const refs = e.pages.map((u) => `[link](${u})`).join(' ');
    lines.push(`| ${escapePipes(e.method)} | ${escapePipes(e.path)} | ${refs} |`);
  }
  lines.push('');
  lines.push('## Full documentation by page');
  lines.push('');

  for (const p of sortedPages) {
    const heading = p.title ? p.title : p.url;
    lines.push(`### ${heading}`);
    lines.push('');
    lines.push(`Source: ${p.url}`);
    lines.push('');
    if (p.endpoints.length) {
      lines.push('Endpoints found on this page:');
      lines.push('');
      for (const e of p.endpoints) lines.push(`- \`${e.method} ${e.path}\``);
      lines.push('');
    }
    lines.push(p.markdown.trim());
    lines.push('');
    lines.push('---');
    lines.push('');
  }

  await fs.writeFile(OUTPUT_MD_PATH, compactEmptyLines(lines.join('\n')), 'utf8');
  await fs.writeFile(
    OUTPUT_ENDPOINTS_JSON_PATH,
    JSON.stringify(
      {
        generatedAt: new Date().toISOString(),
        source: START_URL,
        licensingNotice: GENERATED_NOTICE,
        pages: sortedPages,
        endpointIndex,
      },
      null,
      2,
    ) + '\n',
    'utf8',
  );

  process.stdout.write(
    `Generated ${OUTPUT_MD_PATH} with ${sortedPages.length} pages and ${endpointIndex.length} unique endpoints.\n`,
  );
}

main().catch((err) => {
  console.error(err);
  process.exitCode = 1;
});
