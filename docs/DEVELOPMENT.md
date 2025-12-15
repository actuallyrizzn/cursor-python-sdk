## Development

### Requirements

- Python 3.10+
- Node.js 20+ (for regenerating docs)

### Install (editable)

```bash
python -m pip install -e "./python[dev]"
```

### Run tests

```bash
python -m pytest -q /workspace/python/tests
```

### Regenerate API documentation

The repository includes a generator that crawls Cursor’s docs and writes:

- `docs/api.md`
- `docs/api-endpoints.json`

```bash
npm ci
node scripts/generate-cursor-api-doc.mjs
```

After regeneration, run tests. The integration test `python/tests/integration/test_all_endpoints_covered.py` enforces that the SDK’s `ENDPOINT_SPECS` matches documented endpoints.
