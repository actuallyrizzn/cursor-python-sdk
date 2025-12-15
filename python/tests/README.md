# Test Organization

This directory contains tests organized into three categories:

## Unit Tests (`unit/`)

Unit tests test individual components in isolation, typically using mocks. These tests:
- Test specific methods and functions
- Use `httpx.MockTransport` to simulate HTTP responses
- Run quickly and don't require network access
- Examples: `test_auth.py`, `test_request_handling.py`

## Integration Tests (`integration/`)

Integration tests verify that multiple components work together correctly. These tests:
- Test the interaction between the SDK and the API structure
- May use mocks but test real API endpoint coverage
- Verify that the SDK correctly implements all documented endpoints
- Examples: `test_all_endpoints_covered.py`, `test_auth_types.py`

## End-to-End Tests (`e2e/`)

End-to-end tests verify the complete flow using a real HTTP server. These tests:
- Start an actual HTTP server (e.g., `HTTPServer`)
- Test the full request/response cycle
- Verify behavior in a more realistic environment
- Examples: `test_local_server_e2e.py`

## Running Tests

Run all tests:
```bash
python -m pytest tests/
```

Run by category:
```bash
python -m pytest tests/unit/
python -m pytest tests/integration/
python -m pytest tests/e2e/
```

