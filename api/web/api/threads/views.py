from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from loguru import logger
from openai import OpenAI

from api.db.dao.message import list_messages_by_thread
from api.db.dao.thread import create_thread, get_thread, list_threads_by_user
from api.db.models import Message, Thread, User
from api.services.fastapi_user_manager import current_active_user
from api.utils.response import GenericMultipleResponse, GenericSingleResponse
from api.web.api.threads.schema import MessageInputDTO, ThreadInputDTO

client = OpenAI()
router = APIRouter()


@router.post("/", response_model=GenericSingleResponse[Thread], tags=["Threads"])
async def create(
    new_thread_object: ThreadInputDTO, user: User = Depends(current_active_user),
):
    thread = client.beta.threads.create()
    logger.info("[ OpenAI ] thread created - {thread_id}", thread_id=thread.id)

    thread_db = await create_thread(
        _id=thread.id, title=new_thread_object.title, user=user,
    )

    return {"code": HTTPStatus.CREATED, "data": thread_db}


@router.get("/", response_model=GenericMultipleResponse[Thread], tags=["Threads"])
async def list_mine(user: User = Depends(current_active_user)):
    threads = await list_threads_by_user(user.id)
    return {"code": HTTPStatus.OK, "data": threads}


@router.get(
    "/{thread_id}",
    dependencies=[Depends(current_active_user)],
    response_model=GenericSingleResponse[Thread],
    tags=["Threads"],
)
async def get_thread_by_id(thread_id: str):
    thread = await get_thread(thread_id)
    return {"code": HTTPStatus.OK if thread else HTTPStatus.NOT_FOUND, "data": thread}


@router.post(
    "/{thread_id}/messages",
    dependencies=[Depends(current_active_user)],
    tags=["Messages"],
)
async def create_thread_message(thread_id: str, new_message_object: MessageInputDTO):
    message = client.beta.threads.messages.create(
        thread_id=thread_id, role="user", content=new_message_object.content,
    )
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread_id, assistant_id=new_message_object.assistant_id,
    )

    if run.status == "completed":
        messages = client.beta.threads.messages.list(thread_id=thread_id)
        return {"data": messages}
    else:
        logger.info("[ OPENAI ] Run status - {status}", status=run.status)


@router.get(
    "/{thread_id}/messages",
    dependencies=[Depends(current_active_user)],
    response_model=GenericMultipleResponse[Message],
    tags=["Messages"],
)
async def list_messages(thread_id: str):
    if thread_id is None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail="Missing parameter thread_id",
        )

    messages = await list_messages_by_thread(thread_id)
    return {"code": HTTPStatus.OK, "data": messages}
