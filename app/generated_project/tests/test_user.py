from fastapi.testclient import TestClient
from user import router as user_router

client = TestClient(user_router)

def test_apply_leave():
    response = client.post("/api/lms/leaves/apply", json={"start_date": "2022-01-01", "end_date": "2022-01-10", "reason": "vacation"})
    assert response.status_code == 200

def test_get_leave_status():
    response = client.get("/api/lms/leaves/status")
    assert response.status_code == 200
