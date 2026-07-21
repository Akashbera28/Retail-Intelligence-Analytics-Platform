from fastapi import FastAPI

from app.config.settings import settings
from app.database import init_db
from app.routers import api_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)


@app.on_event("startup")
def startup():
    init_db()


# Register all API routers
app.include_router(api_router)


@app.get("/")
def root():
    return {
        "message": f"{settings.APP_NAME} v{settings.APP_VERSION} is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }