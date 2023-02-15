from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from backend.models.database import get_async_session
from backend.models.grows import Grow
from backend.models.users import User
from backend.routes.dependencies import current_active_user
from backend.schemas.grows import GrowCreate, GrowDB


router = APIRouter(prefix="/grows", tags=["grows"])


@router.get("/", response_model=List[GrowDB])
async def list(
    session: AsyncSession = Depends(get_async_session),
    skip: int = 0,
    limit: int = 100,
    # current_user: User = Depends(current_active_user),
) -> Any:
    return await Grow.objects().all(session)


@router.post("/", response_model=GrowDB)
async def create(
    instance: GrowCreate,
    session: AsyncSession = Depends(get_async_session),
    # current_user: User = Depends(current_active_user),
) -> Any:
    return await Grow.objects().create(instance).save(session)


@router.get("/{instance_id}", response_model=GrowDB)
async def read(
    instance_id: int,
    session: AsyncSession = Depends(get_async_session),
    skip: int = 0,
    limit: int = 100,
    # current_user: User = Depends(current_active_user),
) -> Any:
    return await Grow.objects().filter(id=instance_id).first(session)
