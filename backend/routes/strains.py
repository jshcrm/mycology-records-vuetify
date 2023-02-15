from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from backend.models.database import get_async_session
from backend.models.strains import Strain
from backend.models.users import User
from backend.routes.dependencies import current_active_user
from backend.schemas.strains import StrainCreate, StrainDB


router = APIRouter(prefix="/strain", tags=["strain"])


@router.get("/", response_model=List[StrainDB])
async def read_strains(
    session: AsyncSession = Depends(get_async_session),
    skip: int = 0,
    limit: int = 100,
    # current_user: User = Depends(current_active_user),
) -> Any:
    """
    Retrieve strain.
    """
    return await Strain.objects().all(session)


@router.post("/", response_model=StrainDB)
async def create_strain(
    instance: StrainCreate,
    session: AsyncSession = Depends(get_async_session),
    # current_user: User = Depends(current_active_user),
) -> Any:
    """
    Create strains
    """
    return await Strain.objects().create(instance).save(session)
