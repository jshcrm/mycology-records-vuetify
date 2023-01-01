from os import environ

from pydantic import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = environ.get("DEBUG", "False") == True

    SECRET: str = environ.get("SECRET", "")

    DATABASE_HOST: str = environ.get("DATABASE_HOST", "")
    DATABASE_PORT: str = environ.get("DATABASE_PORT", "")
    DATABASE_DB: str = environ.get("DATABASE_DB", "")
    DATABASE_USER: str = environ.get("DATABASE_USER", "")
    DATABASE_PASSWORD: str = environ.get("DATABASE_PASSWORD", "")

    MEDIA_DIR: str = f"/media"

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DATABASE_USER}@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_DB}"
