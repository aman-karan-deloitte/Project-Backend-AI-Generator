from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from database import SessionLocal, engine
from database import User, Leave, Pod
from typing import List

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/login")
def login(user: OAuth2PasswordRequestForm = Depends()):
    db = SessionLocal()
    user_obj = db.query(User).filter(User.email == user.username).first()
    if not user_obj:
        return JSONResponse({"error": "User not found"}, status_code=401)
    if not user_obj.password == user.password:
        return JSONResponse({"error": "Password incorrect"}, status_code=401)
    return JSONResponse({"access_token": user_obj.email, "token_type": "bearer"})

@app.get("/api/auth/user")
def get_user(db: SessionLocal = Depends(get_db), token: str = Depends(oauth2_scheme)):
    user_obj = db.query(User).filter(User.email == token).first()
    return user_obj
