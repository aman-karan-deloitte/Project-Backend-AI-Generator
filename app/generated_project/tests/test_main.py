from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_login():
    response = client.post("/login", data={"username": "user", "password": "password"})
    assert response.status_code == 200

def test_get_user():
    response = client.get("/api/auth/user", headers={"Authorization": "Bearer token"})
    assert response.status_code == 200
