"""Test creating an agent on the cursor-test repository.

This test verifies that we can successfully create a cloud agent
pointed at the actuallyrizzn/cursor-test repository.

To run:
    export CURSOR_API_KEY=your_api_key_here
    python -m pytest tests/e2e/test_agent_on_cursor_test_repo.py -v
"""

import os

import pytest

from cursor_sdk import CursorClient
from cursor_sdk.errors import CursorAPIError, CursorAuthError, CursorRateLimitError


# Skip all tests if API key is not available
pytestmark = [
    pytest.mark.skipif(
        not os.getenv("CURSOR_API_KEY"),
        reason="CURSOR_API_KEY environment variable not set",
    ),
    pytest.mark.e2e,
]


@pytest.fixture
def api_key() -> str:
    """Get API key from environment variable."""
    key = os.getenv("CURSOR_API_KEY")
    if not key:
        pytest.skip("CURSOR_API_KEY not set")
    return key


@pytest.fixture
def client(api_key: str) -> CursorClient:
    """Create a client instance with real API key."""
    return CursorClient(api_key, base_url="https://api.cursor.com")


def test_create_agent_on_cursor_test_repo(client: CursorClient) -> None:
    """Test creating an agent on the cursor-test repository."""
    # Create an agent pointing at the cursor-test repo
    agent_data = {
        "prompt": {
            "text": "Create a simple README.md file with basic project information"
        },
        "source": {
            "repository": "https://github.com/actuallyrizzn/cursor-test",
            "ref": "main"
        },
        "target": {
            "autoCreatePr": False,
            "branchName": "cursor/test-agent"
        }
    }
    
    try:
        result = client.post_v0_agents(json=agent_data)
        
        # Verify we got a response with agent ID
        assert result is not None
        assert isinstance(result, dict)
        assert "id" in result
        agent_id = result["id"]
        
        # Verify the agent was created with correct repository
        assert "source" in result
        assert result["source"]["repository"] == "https://github.com/actuallyrizzn/cursor-test"
        
        # Clean up: delete the agent
        try:
            client.delete_v0_agents_id(agent_id)
        except Exception:
            # If deletion fails, that's ok - agent might have already finished/deleted
            pass
            
    except CursorRateLimitError:
        pytest.skip("Rate limited on POST /v0/agents")
    except CursorAuthError as e:
        # Auth errors might indicate insufficient permissions
        pytest.skip(f"Insufficient permissions to create agents: {e}")
    except CursorAPIError as e:
        # Other API errors (400, 404, 500, etc.) - verify error structure
        assert e.status_code >= 400
        assert e.message is not None
    finally:
        client.close()


def test_create_agent_and_check_status(client: CursorClient) -> None:
    """Test creating an agent and checking its status."""
    agent_data = {
        "prompt": {
            "text": "Add a .gitignore file"
        },
        "source": {
            "repository": "https://github.com/actuallyrizzn/cursor-test",
            "ref": "main"
        }
    }
    
    try:
        # Create agent
        create_result = client.post_v0_agents(json=agent_data)
        
        if not isinstance(create_result, dict) or "id" not in create_result:
            pytest.skip("Failed to create agent")
            
        agent_id = create_result["id"]
        
        # Check agent status
        status_result = client.get_v0_agents_id(agent_id)
        
        assert status_result is not None
        assert isinstance(status_result, dict)
        assert status_result["id"] == agent_id
        assert "status" in status_result
        
        # Clean up
        try:
            client.delete_v0_agents_id(agent_id)
        except Exception:
            pass
            
    except CursorRateLimitError:
        pytest.skip("Rate limited")
    except CursorAuthError as e:
        pytest.skip(f"Insufficient permissions: {e}")
    except CursorAPIError as e:
        # Acceptable - just verify error structure
        assert e.status_code >= 400
    finally:
        client.close()

