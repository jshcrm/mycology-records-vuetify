import asyncio

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes.routes import add_routes_to_app
from .services.queue import procrastinate_app
from .settings import Settings

settings = Settings()

openapi_url = "/openapi.json" if settings.DEBUG else None
docs_url = "/docs" if settings.DEBUG else None
redoc_url = "/redoc" if settings.DEBUG else None

app = FastAPI(openapi_url=openapi_url, docs_url=docs_url, redoc_url=redoc_url)

origins = [
    "http://localhost:8082",
    "https://localhost:8082",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def on_startup():
    await procrastinate_app.open_async()

    if settings.IS_TASK_QUEUE:
        asyncio.create_task(
            procrastinate_app.run_worker_async(concurrency=4, delete_jobs="successful")
        )


@app.on_event("shutdown")
async def shutdown() -> None:
    await procrastinate_app.close_async()


from .models.imports import *

add_routes_to_app(app)
