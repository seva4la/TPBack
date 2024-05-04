from fastapi import APIRouter

from api.users import router as user_router
from api.categories import router as categories_router

router = APIRouter()

router.include_router(user_router)
router.include_router(categories_router)

