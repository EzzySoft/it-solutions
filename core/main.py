from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from api import router_api_v1
from config import settings
from models import database_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await database_helper.dispose()


main_app = FastAPI(
    title="IT Solutions Service API",
    version="0.1.0",
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",
    lifespan=lifespan,
)

main_app.include_router(router_api_v1, prefix=settings.api.prefix)

if __name__ == "__main__":
    uvicorn.run(
        "main:main_app", host=settings.run.host, port=settings.run.port, reload=True
    )
