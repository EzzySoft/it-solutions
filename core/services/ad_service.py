import hashlib
import random

import bcrypt
import redis.asyncio as redis
from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession

from config import settings
from crud import user_crud, ad_crud
from exceptions import (
    InvalidSessionError,
    InvalidCredentialsError,
)
from schemas.ad_scheme import AdvertisementScheme
from schemas.user_scheme import (
    CredentialsScheme,
    CreateUserScheme,
    UserScheme,
)
from services import auth_service


async def get(ad_id: int, request: Request, db: AsyncSession) -> AdvertisementScheme:
    user = await auth_service.get_info(request=request, db=db)
    print(f"User {user.username} searching for {ad_id}.")

    return await ad_crud.get(ad_id=ad_id, db=db)
