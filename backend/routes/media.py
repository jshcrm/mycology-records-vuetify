from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from backend.models.database import get_async_session
from backend.models.media import Media
from backend.models.users import User
from backend.routes.dependencies import current_active_user
from backend.schemas.media import MediaCreate, MediaDB


router = APIRouter(prefix="/media", tags=["media"])


@router.get("/", response_model=List[MediaDB])
async def read(
    session: AsyncSession = Depends(get_async_session),
    skip: int = 0,
    limit: int = 100,
    # current_user: User = Depends(current_active_user),
) -> Any:
    return await Media.objects().filter(session)


@router.post("/", response_model=MediaDB)
async def create(
    instance: MediaCreate,
    session: AsyncSession = Depends(get_async_session),
    # current_user: User = Depends(current_active_user),
) -> Any:
    return await Media.objects().create(instance).save(session)


@router.delete("/{instance_id}")
async def delete(
    instance_id: int,
    session: AsyncSession = Depends(get_async_session),
    skip: int = 0,
    limit: int = 100,
    # current_user: User = Depends(current_active_user),
) -> Any:
    await Media.objects().filter(id=instance_id).delete(session)
    return JSONResponse(status_code=204, content={"status": "success"})
