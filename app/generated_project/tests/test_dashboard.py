import pytest
from app.main import app
@pytest.fixture
def test_app():
    return app

def test_get_dashboard_data():
    response = test_app().get("/api/dashboard/tiles")
    assert response.status_code == 200