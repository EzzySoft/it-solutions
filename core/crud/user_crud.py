import re
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import bcrypt

from config import settings
from exceptions import UsernameInUseError, EmailInUseError, UserNotFoundError
from schemas.user_scheme import CreateUserScheme, UserScheme
from models.user import User


async def create(user_create: CreateUserScheme, db: AsyncSession) -> UserScheme:
    async def check_username(username: str) -> None:
        user: User = (
            (await db.execute(select(User).where(User.username == username)))
            .scalars()
            .first()
        )

        if user:
            raise UsernameInUseError

    async def check_email(email: str) -> None:
        user: User = (
            (await db.execute(select(User).where(User.email == email)))
            .scalars()
            .first()
        )

        if user:
            raise EmailInUseError

    await check_username(username=user_create.username)
    await check_email(email=user_create.email)

    hashed_password = None
    if user_create.password:
        hashed_password = bcrypt.hashpw(
            user_create.password.encode("utf-8"), bcrypt.gensalt()
        )

    new_user: User = User(
        email=user_create.email,
        username=user_create.username,
        password_hash=hashed_password,
    )

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    user_scheme: UserScheme = UserScheme(**new_user.__dict__)

    return user_scheme


async def get(param, db: AsyncSession) -> UserScheme:
    if isinstance(param, int):
        stmt = select(User).where(User.user_id == param)
    else:
        if re.match(settings.validation.email_pattern, param) is not None:
            stmt = select(User).where(User.email == param)
        else:
            stmt = select(User).where(User.username == param)

    user = (await db.execute(stmt)).scalars().first()

    if not user:
        raise UserNotFoundError

    user_scheme: UserScheme = UserScheme(**user.__dict__)
    return user_scheme


async def get_hash(user_id: int, db: AsyncSession) -> bytes:
    query = select(User).filter(User.user_id == user_id)
    result = await db.execute(query)
    user = result.scalars().first()
    if user:
        return user.password_hash
    raise UserNotFoundError
