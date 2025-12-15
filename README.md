## Cursor endpoint SDK (Python)

A small, synchronous Python client for Cursor’s public APIs.

- **API base URL**: `https://api.cursor.com`
- **Transport**: `httpx`
- **Docs snapshot**: `docs/api.md` (generated)

### Install

```bash
python -m pip install cursor-endpoint-sdk
```

### Quickstart

```python
from cursor_sdk import CursorClient
from cursor_sdk.errors import CursorAPIError

with CursorClient("YOUR_API_KEY") as client:
    try:
        me = client.get_v0_me()
        print(me)
    except CursorAPIError as e:
        # Includes status_code, message, and (when available) body/headers.
        raise
```

### Authentication

The Cursor API supports both Basic and Bearer auth. By default the SDK uses **Basic auth** with your API key as the username and an empty password (matching the official docs’ `curl -u YOUR_API_KEY:` examples).

```python
# Basic (default)
client = CursorClient("YOUR_API_KEY", auth="basic")

# Bearer
client = CursorClient("YOUR_API_KEY", auth="bearer")
```

### Calling endpoints

`CursorClient` exposes one method per documented endpoint. Method names are derived from the HTTP method + path, for example:

- `GET /teams/members` → `client.get_teams_members()`
- `POST /teams/spend` → `client.post_teams_spend(json={...})`
- `GET /analytics/ai-code/commits.csv` → `client.get_analytics_ai_code_commits_csv()`

Common kwargs:

- `params`: query parameters
- `json`: JSON body (for `POST`/`PATCH`)
- `headers`: per-request headers
- `timeout`: per-request timeout override

```python
from cursor_sdk import CursorClient

with CursorClient("YOUR_API_KEY") as client:
    members = client.get_teams_members()
    spend = client.post_teams_spend(json={"page": 1, "pageSize": 25})
    audit = client.get_teams_audit_logs(params={"startTime": "7d", "endTime": "now"})
```

### Response handling

- **JSON** responses return Python objects (`dict` / `list`).
- **CSV** endpoints return a `str` when the response content-type is `text/csv` or the path ends with `.csv`.
- Empty bodies and `304 Not Modified` return `None`.

### Errors

The SDK raises typed exceptions:

- `CursorAuthError` for **401/403**
- `CursorRateLimitError` for **429**
- `CursorAPIError` for other **non-2xx** API responses
- `CursorNetworkError` for network/transport failures

### Generated API docs + endpoint coverage

This repo includes a crawler that snapshots Cursor’s public API docs:

```bash
npm ci
node scripts/generate-cursor-api-doc.mjs
```

It writes:

- `docs/api.md` (human-readable)
- `docs/api-endpoints.json` (machine-readable)

The integration test `python/tests/integration/test_all_endpoints_covered.py` ensures the SDK covers **exactly** the documented endpoints.

### Development

```bash
python -m pip install -e "./python[dev]"
python -m pytest -q /workspace/python/tests
```

### Licensing

- **Code**: AGPLv3 (**AGPL-3.0-only**) — see `LICENSE`.
- **All other content**: CC BY-SA 4.0 (**CC-BY-SA-4.0**) — see `LICENSES/CC-BY-SA-4.0.txt`.

See `LICENSING.md` for details and notes about generated documentation.

### Disclaimer

This project is not affiliated with, endorsed by, or sponsored by Cursor.
