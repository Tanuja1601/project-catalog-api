from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.projects import router as projects_router
from app.api.routes.version import router as version_router
from app.core.config import get_settings
from app.core.database import init_db


@asynccontextmanager
async def lifespan(_: FastAPI):
    init_db()
    yield


def create_app() -> FastAPI:
    settings = get_settings()
    application = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        lifespan=lifespan,
        docs_url="/docs",
        redoc_url="/redoc",
    )

    application.include_router(health_router, prefix="/api/v1", tags=["health"])
    application.include_router(version_router, prefix="/api/v1", tags=["version"])
    application.include_router(projects_router, prefix="/api/v1", tags=["projects"])

    return application


app = create_app()
