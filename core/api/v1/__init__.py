from fastapi import APIRouter
from config import settings

from .auth import router as auth_router
from .advertisement import router as ad_router

router = APIRouter(prefix=settings.api.v1.prefix)

router.include_router(router=auth_router, prefix=settings.api.v1.auth)
router.include_router(router=ad_router, prefix=settings.api.v1.ad_router)
