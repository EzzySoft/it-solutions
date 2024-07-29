import hashlib
import random

import bcrypt
import redis.asyncio as redis
from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession

from config import settings
from crud import user_crud
from exceptions import (
    InvalidSessionError,
    InvalidCredentialsError,
)
from schemas.user_scheme import (
    CredentialsScheme,
    CreateUserScheme,
    UserScheme,
)


async def register_user(user_create: CreateUserScheme, db: AsyncSession) -> dict:
    await user_crud.create(user_create, db)

    return {"message": "User registered successfully"}


async def login_user(user_login: CredentialsScheme, db: AsyncSession) -> dict:
    user_data = await authenticate_user(user_login, db)
    session_id = await create_session(user_data.user_id, user_data.username)

    return {"message": "Logged in successfully", "session_id": session_id}


async def authenticate_user(
    credentials: CredentialsScheme, db: AsyncSession
) -> UserScheme:
    user_data: UserScheme = await user_crud.get(credentials.login, db)

    if not bcrypt.checkpw(
        credentials.password.encode("utf-8"), user_data.password_hash
    ):
        raise InvalidCredentialsError()

    return user_data


async def create_session(user_id: int, username: str) -> str:
    session_id = hashlib.sha256(f"{user_id}{random.random()}".encode()).hexdigest()
    user_data = {"username": username, "user_id": user_id}

    async with redis.from_url(f"redis://{settings.redis.host}") as redis_client:
        await redis_client.hset(f"session:{session_id}", mapping=user_data)
        await redis_client.expire(f"session:{session_id}", settings.redis.expire_time)

        return session_id


async def get_info(request: Request, db: AsyncSession):
    user = await get_user_from_session_id(request, db)
    user.__dict__.pop("password_hash")
    return user


async def get_user_from_session_id(request: Request, db: AsyncSession) -> UserScheme:
    session_id: str = request.cookies.get("session_id")
    if not session_id:
        raise InvalidSessionError

    async with redis.from_url(f"redis://{settings.redis.host}") as redis_client:
        username = await redis_client.hget(f"session:{session_id}", "username")

        if not username:
            raise InvalidSessionError
        user_data: UserScheme = await user_crud.get(username.decode("utf-8"), db)

        return user_data


async def get_session_id(request: Request):
    session_id = request.cookies.get("session_id")

    async with redis.from_url(f"redis://{settings.redis.host}") as redis_client:

        if not session_id or not await redis_client.exists(f"session:{session_id}"):
            raise InvalidSessionError
        return session_id


async def logout(request: Request):
    session_id = await get_session_id(request)
    async with redis.from_url(f"redis://{settings.redis.host}") as redis_client:
        await redis_client.delete(f"session:{session_id}")

        return {"message": "Logged out successfully"}
