from fastapi import FastAPI

from app.config.settings import settings


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)


@app.get("/")
def root():
    return {
        "message": f"{settings.APP_NAME} v{settings.APP_VERSION} is running"
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}