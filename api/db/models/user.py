from beanie import Document, PydanticObjectId
from fastapi_users import schemas
from fastapi_users.db import BeanieBaseUser
from fastapi_users_db_beanie import BeanieUserDatabase


class User(BeanieBaseUser, Document):
    pass


class UserRead(schemas.BaseUser[PydanticObjectId]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass


async def get_user_db():
    yield BeanieUserDatabase(User)
