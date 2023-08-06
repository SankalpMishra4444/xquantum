# app/api/api_v1/api.py
from fastapi import APIRouter

from app.api.endpoints import item, user

api_router = APIRouter()

api_router.include_router(item.router, tags=["items"], prefix="/items")
api_router.include_router(user.router, tags=["users"], prefix="/users")
