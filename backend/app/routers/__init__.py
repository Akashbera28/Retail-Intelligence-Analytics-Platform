from fastapi import APIRouter

from app.routers.auth import router as auth_router
from app.routers.users import router as users_router
from app.routers.upload import router as upload_router
from app.routers.analytics import router as analytics_router

api_router = APIRouter()

api_router.include_router(auth_router)
api_router.include_router(users_router)
api_router.include_router(upload_router)
api_router.include_router(analytics_router)

__all__ = [
    "api_router",
]