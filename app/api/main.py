from fastapi import APIRouter

from app.api.routes import users, groups

api_router = APIRouter()
api_router.include_router(users.router)
api_router.include_router(groups.router)