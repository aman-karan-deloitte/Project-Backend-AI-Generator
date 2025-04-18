import pytest
from app.main import app
@pytest.fixture
def test_app():
    return app

def test_apply_for_leave():
    response = test_app().post("/api/lms/leaves/apply")
    assert response.status_code == 200

def test_get_leave_status():
    response = test_app().get("/leave/status")
    assert response.status_code == 200

def test_approve_leave():
    response = test_app().patch("/leave/approve/1")
    assert response.status_code == 200