from typing import Dict, List

from fastapi import APIRouter
from fastapi.param_functions import Depends

from api.db.dao.dummy_dao import DummyDAO
from api.db.models.dummy_model import Dummy
from api.db.models.user import User
from api.services.fastapi_user_manager import current_active_user
from api.web.api.dummy.schema import DummyModelDTO, DummyModelInputDTO

router = APIRouter()


@router.get("/", response_model=Dict[str, List[DummyModelDTO] | str])
async def get_dummy_models(
    limit: int = 10,
    offset: int = 0,
    dummy_dao: DummyDAO = Depends(),
    user: User = Depends(current_active_user),
) -> Dict[str, List[Dummy] | str]:
    """
    Retrieve all dummy objects from the database.

    :param limit: limit of dummy objects, defaults to 10.
    :param offset: offset of dummy objects, defaults to 0.
    :param dummy_dao: DAO for dummy models.
    :return: list of dummy objects from database.
    """
    dummies = await dummy_dao.get_all_dummies(limit=limit, offset=offset)
    return {
        "user": user.email,
        "data": dummies,
    }


@router.put("/")
async def create_dummy_model(
    new_dummy_object: DummyModelInputDTO,
    dummy_dao: DummyDAO = Depends(),
) -> None:
    """
    Creates dummy model in the database.

    :param new_dummy_object: new dummy model item.
    :param dummy_dao: DAO for dummy models.
    """
    await dummy_dao.create_dummy_model(name=new_dummy_object.name)
