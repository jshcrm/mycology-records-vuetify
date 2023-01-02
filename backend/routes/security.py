from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy,
)

bearer_transport = BearerTransport(tokenUrl="users/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret="", lifetime_seconds=None)


jwt_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

auth_backends = [jwt_backend]
