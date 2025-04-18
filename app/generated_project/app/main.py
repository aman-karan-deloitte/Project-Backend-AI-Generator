from fastapi import FastAPI
app = FastAPI()

from app.api.routes import user, item

app.include_router(user.router)
app.include_router(item.router)

from app.api.routes import dashboard, lms, pods, auth

app.include_router(dashboard.router)
app.include_router(lms.router)
app.include_router(pods.router)
app.include_router(auth.router)