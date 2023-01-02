from typing import Optional

from fastapi_users import schemas


class UserDB(schemas.BaseUser[int]):
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class UserCreate(schemas.BaseUserCreate):
    is_active: Optional[bool]
    is_superuser: Optional[bool]
    is_verified: Optional[bool]
    is_staff: Optional[bool]


class UserUpdate(schemas.BaseUserUpdate):
    is_active: Optional[bool]
    is_superuser: Optional[bool]
    is_verified: Optional[bool]
    is_staff: Optional[bool]
    password: Optional[str]

    class Config:
        orm_mode = True
