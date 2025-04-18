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

@router.post("/api/lms/leaves/apply")
def apply_leave(user: User, db: SessionLocal = Depends(get_db), token: str = Depends(oauth2_scheme)):
    user_obj = db.query(User).filter(User.email == token).first()
    if not user_obj:
        return JSONResponse({"error": "User not found"}, status_code=401)
    leave_obj = Leave(user_id=user_obj.id, start_date=user.start_date, end_date=user.end_date, reason=user.reason)
    db.add(leave_obj)
    db.commit()
    return JSONResponse({"message": "Leave applied successfully"})

@router.get("/api/lms/leaves/status")
def get_leave_status(db: SessionLocal = Depends(get_db), token: str = Depends(oauth2_scheme)):
    user_obj = db.query(User).filter(User.email == token).first()
    if not user_obj:
        return JSONResponse({"error": "User not found"}, status_code=401)
    leave_obj = db.query(Leave).filter(Leave.user_id == user_obj.id).first()
    return JSONResponse({"status": leave_obj.status})
