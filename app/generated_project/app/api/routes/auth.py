from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer
router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
@router.post("/api/auth/login")
def login():
    return {"token": "access_token"}
@router.get("/api/auth/user")
def get_user():
    return {"id": 1, "name": "John"}