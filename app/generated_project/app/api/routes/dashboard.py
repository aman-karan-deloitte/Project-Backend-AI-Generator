from fastapi import APIRouter
router = APIRouter()
@router.get("/api/dashboard/tiles")
def get_dashboard_data():
    return [{"id": 1, "name": "Tile1"}]