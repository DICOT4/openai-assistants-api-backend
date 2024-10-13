from fastapi import APIRouter

from api.db.models.user import UserCreate, UserRead
from api.services.fastapi_user_manager import auth_backend, fastapi_users

router = APIRouter()

router.include_router(fastapi_users.get_auth_router(auth_backend), prefix="/jwt")

router.include_router(fastapi_users.get_register_router(UserRead, UserCreate))

router.include_router(fastapi_users.get_reset_password_router())

router.include_router(fastapi_users.get_verify_router(UserRead))
