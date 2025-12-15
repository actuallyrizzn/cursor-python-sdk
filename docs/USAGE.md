## SDK usage

The Python SDK lives in `python/src/cursor_sdk` and exposes a synchronous `CursorClient`.

### Install

```bash
python -m pip install cursor-endpoint-sdk
```

### Quickstart

```python
from cursor_sdk import CursorClient

client = CursorClient("YOUR_API_KEY")
try:
    me = client.get_v0_me()
    print(me)
finally:
    client.close()
```

### Authentication

The API supports two auth modes:

- `auth="basic"` (default): sends `Authorization: Basic <base64(api_key + ':')>`
- `auth="bearer"`: sends `Authorization: Bearer <api_key>`

```python
client = CursorClient("YOUR_API_KEY", auth="basic")
```

### Requests

- **Query params**: pass `params={...}`
- **JSON bodies**: pass `json={...}` (primarily for `POST` / `PATCH`)

```python
client.post_teams_spend(json={"page": 1, "pageSize": 25})
client.get_teams_audit_logs(params={"startTime": "7d", "endTime": "now"})
```

### Responses

- JSON responses return Python objects (`dict` / `list`).
- CSV endpoints (content-type `text/csv` or `*.csv` paths) return a `str`.
- Empty bodies and `304 Not Modified` return `None`.

### Errors

Errors are raised as:

- `CursorAuthError` for 401/403
- `CursorRateLimitError` for 429
- `CursorAPIError` for other non-2xx responses
- `CursorNetworkError` for transport-level failures
