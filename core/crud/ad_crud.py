from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from exceptions import AdNotFoundError
from models import Advertisement
from schemas.ad_scheme import AdvertisementScheme


async def get(ad_id: int, db: AsyncSession) -> AdvertisementScheme:
    ad = (
        (await db.execute(select(Advertisement).where(Advertisement.ad_id == ad_id)))
        .scalars()
        .first()
    )

    if not ad:
        raise AdNotFoundError

    return AdvertisementScheme(**ad.__dict__)
