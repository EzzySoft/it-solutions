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


async def get_all(db: AsyncSession) -> list[AdvertisementScheme]:

    ads = (await db.execute(select(Advertisement))).scalars().all()

    ads_list = [AdvertisementScheme(**ad.__dict__) for ad in ads]

    return ads_list
