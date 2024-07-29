from fastapi import APIRouter, Depends
from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession

from models import database_helper
from services import ad_service
from services.response_service import ResponseService

router = APIRouter(tags=["Advertisement"])


@router.get("/{ad_id}")
async def get(
    ad_id: int,
    request: Request,
    db: AsyncSession = Depends(database_helper.session_getter),
):
    return await ResponseService.response(
        ad_service.get(ad_id=ad_id, request=request, db=db)
    )


@router.get("/")
async def get_all(
    request: Request,
    db: AsyncSession = Depends(database_helper.session_getter),
):
    return await ResponseService.response(ad_service.get_all(request=request, db=db))
