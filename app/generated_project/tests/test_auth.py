import pytest
from app.main import app
@pytest.fixture
def test_app():
    return app

def test_login():
    response = test_app().post("/api/auth/login")
    assert response.status_code == 200

def test_get_user():
    response = test_app().get("/api/auth/user")
    assert response.status_code == 200