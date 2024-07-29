from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession

from crud import ad_crud
from schemas.ad_scheme import AdvertisementScheme
from services import auth_service


async def get(ad_id: int, request: Request, db: AsyncSession) -> AdvertisementScheme:
    user = await auth_service.get_info(request=request, db=db)
    print(f"User {user.username} searching for {ad_id}.")

    return await ad_crud.get(ad_id=ad_id, db=db)


async def get_all(request: Request, db: AsyncSession) -> list[AdvertisementScheme]:
    user = await auth_service.get_info(request=request, db=db)
    print(f"User {user.username} searching for all available ads.")

    return await ad_crud.get_all(db=db)
