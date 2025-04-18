from fastapi import APIRouter
router = APIRouter()
@router.post("/api/lms/leaves/apply")
def apply_for_leave():
    return {"message": "Leave applied successfully"}
@router.get("/leave/status")
def get_leave_status():
    return {"status": "Pending"}
@router.patch("/leave/approve/{id}")
def approve_leave(id):
    return {"message": "Leave approved successfully"}