from os import environ

from pydantic import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = environ.get("DEBUG", "False") is True

    SECRET: str = environ.get("SECRET", "")

    IS_TASK_QUEUE: bool = environ.get("IS_TASK_QUEUE", "False") is True

    POSTGRES_HOST: str = environ.get("POSTGRES_HOST", "")
    POSTGRES_PORT: str = environ.get("POSTGRES_PORT", "")
    POSTGRES_DB: str = environ.get("POSTGRES_DB", "")
    POSTGRES_USER: str = environ.get("POSTGRES_USER", "")
    POSTGRES_PASSWORD: str = environ.get("POSTGRES_PASSWORD", "")

    MEDIA_DIR: str = environ.get("POSTGRES_PASSWORD", "/media")

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"  # noqa: E501
