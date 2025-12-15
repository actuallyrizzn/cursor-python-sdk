import base64
import json
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

import pytest

from cursor_sdk import CursorClient


class _Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802
        if self.path != "/teams/members":
            self.send_response(404)
            self.end_headers()
            return

        auth = self.headers.get("Authorization")
        expected = "Basic " + base64.b64encode(b"k:").decode("ascii")
        if auth != expected:
            self.send_response(401)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"message": "unauthorized"}).encode("utf-8"))
            return

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"teamMembers": []}).encode("utf-8"))

    def log_message(self, fmt: str, *args) -> None:  # pragma: no cover
        # Silence noisy server logs during tests.
        return


@pytest.fixture
def server_base_url() -> str:
    # Using port 0 lets the OS assign an available port automatically.
    # This avoids port conflicts when running tests in parallel or on CI.
    httpd = HTTPServer(("127.0.0.1", 0), _Handler)
    host, port = httpd.server_address

    t = threading.Thread(target=httpd.serve_forever, daemon=True)
    t.start()

    try:
        yield f"http://{host}:{port}"
    finally:
        httpd.shutdown()
        httpd.server_close()
        t.join(timeout=2.0)  # Shutdown timeout - using explicit float for clarity


def test_real_http_round_trip(server_base_url: str) -> None:
    # e2e test uses HTTP, so we need to allow it for testing
    client = CursorClient("k", base_url=server_base_url, allow_http=True)
    assert client.get_teams_members() == {"teamMembers": []}
    client.close()
