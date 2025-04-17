from fastapi import FastAPI
from app.api.routes import user
from app.api.routes import item

app = FastAPI()

app.include_router(user.router)
app.include_router(item.router)
