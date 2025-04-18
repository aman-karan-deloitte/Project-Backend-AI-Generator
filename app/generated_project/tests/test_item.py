from fastapi.testclient import TestClient
from item import router as item_router

client = TestClient(item_router)

def test_get_pod_details():
    response = client.get("/api/pods/1/details")
    assert response.status_code == 200

def test_recommend_employee():
    response = client.post("/api/pods/1/recommend", json={"user_id": 1})
    assert response.status_code == 200
