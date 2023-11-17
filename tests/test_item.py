from starlette.testclient import TestClient
from src.main import app
from tests.databases.databases import test_database

client = TestClient(app)

@test_database
def test_create_item():
    response = client.post(
        "/items", json={"name": "foo", "password": "fo"}
    )
    assert response.status_code == 200