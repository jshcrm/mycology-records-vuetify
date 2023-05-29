from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from backend.models.database import get_async_session
from backend.models.spawn import Spawn
from backend.models.users import User
from backend.routes.dependencies import current_active_user
from backend.schemas.spawn import SpawnCreate, SpawnDB


router = APIRouter(prefix="/spawn", tags=["spawn"])


@router.get("/", response_model=List[SpawnDB])
async def read_spawn(
    session: AsyncSession = Depends(get_async_session),
    skip: int = 0,
    limit: int = 100,
    # current_user: User = Depends(current_active_user),
) -> Any:
    """
    Retrieve spawn.
    """
    return await Spawn.objects().filter(session)


@router.post("/", response_model=SpawnDB)
async def create_spawn(
    instance: SpawnCreate,
    session: AsyncSession = Depends(get_async_session),
    # current_user: User = Depends(current_active_user),
) -> Any:
    """
    Create Spawn
    """
    return await Spawn.objects().create(instance).save(session)
