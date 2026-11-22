import pytest
from fastapi.testclient import TestClient

from backend.app import app


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client


def _create_session(client, title="New Research"):
    response = client.post("/sessions/", json={"title": title})
    assert response.status_code == 200
    return response.json()


def test_health(client):
    assert client.get("/").status_code == 200


def test_create_and_fetch_session(client):
    session = _create_session(client, "My topic")

    response = client.get(f"/sessions/{session['id']}")

    assert response.status_code == 200
    assert response.json() == {"id": session["id"], "title": "My topic"}


def test_unknown_session_returns_404(client):
    assert client.get("/sessions/999999").status_code == 404
    assert client.get("/sessions/999999/messages").status_code == 404
    assert (
        client.post("/sessions/999999/chat", json={"query": "hi"}).status_code
        == 404
    )


def test_chat_persists_messages_and_renames_session(client):
    session = _create_session(client)
    query = "Find recent papers on retrieval augmented generation for code search"

    response = client.post(f"/sessions/{session['id']}/chat", json={"query": query})

    assert response.status_code == 200
    assert "Mock AI Response" in response.json()["response"]

    messages = client.get(f"/sessions/{session['id']}/messages").json()
    assert [m["role"] for m in messages] == ["user", "assistant"]
    assert messages[0]["content"] == query

    title = client.get(f"/sessions/{session['id']}").json()["title"]
    assert title == query[:60].rstrip() + "..."


def test_custom_title_is_not_overwritten(client):
    session = _create_session(client, "Keep me")

    client.post(f"/sessions/{session['id']}/chat", json={"query": "hello"})

    assert client.get(f"/sessions/{session['id']}").json()["title"] == "Keep me"


def test_sessions_listed_most_recent_first(client):
    first = _create_session(client, "first")
    second = _create_session(client, "second")
    client.post(f"/sessions/{first['id']}/chat", json={"query": "bump"})

    ids = [s["id"] for s in client.get("/sessions/").json()]

    assert ids.index(first["id"]) < ids.index(second["id"])
