from http import HTTPStatus

from fastapi import APIRouter, Depends
from loguru import logger
from openai import OpenAI

from api.db.dao.assistant import (
    create_assistant,
    get_assistant,
    list_assistants_by_user,
)
from api.db.models import Assistant, User
from api.services.fastapi_user_manager import current_active_user
from api.utils.response import GenericMultipleResponse, GenericSingleResponse
from api.web.api.assistants.schema import AssistantInputDTO

client = OpenAI()
router = APIRouter()


@router.post("/", response_model=GenericSingleResponse[Assistant], tags=["Assistants"])
async def create(
    new_assistant_object: AssistantInputDTO, user: User = Depends(current_active_user),
):
    assistant = client.beta.assistants.create(
        name=new_assistant_object.name,
        instructions=new_assistant_object.instructions,
        model=new_assistant_object.model,
        tools=new_assistant_object.tools,
    )
    logger.info(
        "[ OpenAI ] assistant created - {assistant_id}", assistant_id=assistant.id,
    )

    assistant_db = await create_assistant(
        _id=assistant.id,
        name=new_assistant_object.name,
        instructions=new_assistant_object.instructions,
        model=new_assistant_object.model,
        tools=assistant.tools,
        user=user,
    )

    return {"data": assistant_db}


@router.get("/", response_model=GenericMultipleResponse[Assistant], tags=["Assistants"])
async def list_mine(user: User = Depends(current_active_user)):
    assistants = await list_assistants_by_user(user.id)
    return {"data": assistants}


@router.get(
    "/{assistant_id}",
    dependencies=[Depends(current_active_user)],
    response_model=GenericSingleResponse[Assistant],
    tags=["Assistants"],
)
async def get_assistant_by_id(assistant_id: str):
    assistant = await get_assistant(assistant_id)
    return {
        "message": HTTPStatus.OK.phrase if assistant else HTTPStatus.NOT_FOUND.phrase,
        "data": assistant,
    }
