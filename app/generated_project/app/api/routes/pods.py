from fastapi import APIRouter
router = APIRouter()
@router.get("/api/pods/{pod_id}/details")
def get_pod_details(pod_id):
    return {"id": pod_id, "name": "Pod1"}
@router.post("/api/pods/{pod_id}/recommend")
def recommend_employee(pod_id):
    return {"message": "Employee recommended successfully"}