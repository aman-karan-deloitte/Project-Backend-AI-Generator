import pytest
from app.main import app
@pytest.fixture
def test_app():
    return app

def test_get_pod_details():
    response = test_app().get("/api/pods/1/details")
    assert response.status_code == 200

def test_recommend_employee():
    response = test_app().post("/api/pods/1/recommend")
    assert response.status_code == 200