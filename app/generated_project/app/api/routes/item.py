from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from database import SessionLocal, engine
from database import User
from typing import List

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/api/pods/{pod_id}/details")
def get_pod_details(pod_id: int, db: SessionLocal = Depends(get_db), token: str = Depends(oauth2_scheme)):
    user_obj = db.query(User).filter(User.email == token).first()
    if not user_obj:
        return JSONResponse({"error": "User not found"}, status_code=401)
    pod_obj = db.query(Pod).filter(Pod.id == pod_id).first()
    return JSONResponse({"name": pod_obj.name, "members": pod_obj.members})

@router.post("/api/pods/{pod_id}/recommend")
def recommend_employee(pod_id: int, user: User, db: SessionLocal = Depends(get_db), token: str = Depends(oauth2_scheme)):
    user_obj = db.query(User).filter(User.email == token).first()
    if not user_obj:
        return JSONResponse({"error": "User not found"}, status_code=401)
    pod_obj = db.query(Pod).filter(Pod.id == pod_id).first()
    pod_obj.members.append(user.id)
    db.commit()
    return JSONResponse({"message": "Employee recommended successfully"})
