from fastapi import APIRouter

from app.api.routes import users, groups, answers, posts

api_router = APIRouter()
api_router.include_router(users.router)
api_router.include_router(groups.router)
api_router.include_router(answers.router)
api_router.include_router(posts.router)
