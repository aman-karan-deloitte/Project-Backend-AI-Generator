from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

router = APIRouter()

class User(BaseModel):
    id: int
    name: str
    email: str

@router.get("/api/auth/user")
def get_user():
    return {"message": "Hello, World!"}
