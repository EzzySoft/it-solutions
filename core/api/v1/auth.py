from fastapi import APIRouter, Depends
from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession

from models import database_helper
from services import auth_service
from schemas.user_scheme import CreateUserScheme, CredentialsScheme
from services.response_service import ResponseService

router = APIRouter(tags=["Auth"])


@router.post("/signup")
async def sign_up(
    user: CreateUserScheme, db: AsyncSession = Depends(database_helper.session_getter)
):
    return await ResponseService.response(
        auth_service.register_user(user_create=user, db=db)
    )


@router.post("/login")
async def login(
    user: CredentialsScheme, db: AsyncSession = Depends(database_helper.session_getter)
):
    return await ResponseService.response(
        auth_service.login_user(user_login=user, db=db)
    )


@router.post("/logout")
async def logout(request: Request):
    return await ResponseService.response(auth_service.logout(request=request))


@router.get("/check")
async def check(
    request: Request, db: AsyncSession = Depends(database_helper.session_getter)
):
    return await ResponseService.response(auth_service.get_info(request=request, db=db))
