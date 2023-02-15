from ..schemas.users import UserCreate, UserDB, UserUpdate
from .dependencies import fastapi_users
from .security import jwt_backend
from backend.routes import grows, media, strains


def add_routes_to_app(app):
    app.include_router(
        fastapi_users.get_auth_router(jwt_backend),
        prefix="/users/jwt",
        tags=["users"],
    )
    app.include_router(
        fastapi_users.get_register_router(UserDB, UserCreate),
        prefix="/users",
        tags=["users"],
    )
    app.include_router(
        fastapi_users.get_users_router(UserDB, UserUpdate),
        prefix="/users",
        tags=["users"],
    )
    app.include_router(
        fastapi_users.get_verify_router(UserDB),
        prefix="/users",
        tags=["users"],
    )

    # app.include_router(spawn.router)
    app.include_router(strains.router)
    app.include_router(grows.router)
    app.include_router(media.router)
