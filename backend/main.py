from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .models._database import database
from .settings import Settings


settings = Settings()

sentry_dsn = settings.SENTRY_DSN
if sentry_dsn:
    import sentry_sdk
    from sentry_sdk.integrations.starlette import StarletteIntegration
    from sentry_sdk.integrations.fastapi import FastApiIntegration

    sentry_sdk.init(
        dsn=sentry_dsn,
        integrations=[StarletteIntegration(), FastApiIntegration()],
        traces_sample_rate=1.0,
    )

openapi_url = "/openapi.json" if settings.DEBUG else None
docs_url = "/docs" if settings.DEBUG else None
redoc_url = "/redoc" if settings.DEBUG else None

app = FastAPI(openapi_url=openapi_url, docs_url=docs_url, redoc_url=redoc_url)
app.state.database = database

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
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()

@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()

    await procrastinate_app.close_async()

from app.routers._routes import add_routes_to_app
add_routes_to_app(app)
