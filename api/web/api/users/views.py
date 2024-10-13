from fastapi import APIRouter

from api.db.models.user import UserRead, UserUpdate
from api.services.fastapi_user_manager import fastapi_users

router = APIRouter()

router.include_router(fastapi_users.get_users_router(UserRead, UserUpdate))
