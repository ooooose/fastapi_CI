from starlette.testclient import TestClient
from src.main import app
from fastapi import status
from tests.databases.databases import test_database

client = TestClient(app)

@test_database
def test_create_item():
    response = client.post(
        "/items", json={"name": "foo", "description": "bar"}
    )

    assert response.status_code == status.HTTP_200_OK