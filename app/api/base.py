from api.routes import uploadDoc
from fastapi import APIRouter
api_router = APIRouter()
api_router.include_router(uploadDoc.router, prefix="", tags=["upload"])