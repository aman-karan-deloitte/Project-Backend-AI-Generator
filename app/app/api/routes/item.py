from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

router = APIRouter()

class Item(BaseModel):
    id: int
    name: str
    description: str

@router.get("/api/items")
def get_items():
    return {"message": "Hello, World!"}
