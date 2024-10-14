from typing import List, Literal

from api.db.models import Assistant, Message, Thread


async def create_message(
    _id: str,
    content: str,
    role: Literal["user", "assistant"],
    assistant: Assistant,
    thread: Thread,
) -> Message:
    message = Message(
        id=_id, content=content, role=role, assistant=assistant, thread=thread,
    )
    await message.create()
    return message


async def list_messages_by_thread(thread_id: str) -> List[Message]:
    return await Message.find(Message.thread.id == thread_id).to_list()
