# main.py
from fastapi import FastAPI

from app.api.api_v1.api import api_router
from app.core.config import settings

app = FastAPI(title=settings.app_name)

app.include_router(api_router, prefix=settings.api_v1_prefix)