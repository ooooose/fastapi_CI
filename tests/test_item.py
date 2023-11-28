from starlette.testclient import TestClient
from src.main import app
from fastapi import status
from tests.conftest import override_session_factory
from src.db import session_factory

client = TestClient(app)

app.dependency_overrides[session_factory] = override_session_factory


def test_create_item():
    response = client.post("/items", json={"name": "foo", "description": "bar"})

    assert response.status_code == status.HTTP_200_OK
