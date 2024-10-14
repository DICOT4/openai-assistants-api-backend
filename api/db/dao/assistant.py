from typing import List, Optional

from beanie import PydanticObjectId
from openai.types.beta import AssistantTool

from api.db.models import Assistant, User


async def create_assistant(
    _id: str,
    name: str,
    instructions: str,
    model: str,
    tools: Optional[List[AssistantTool]],
    user: User,
) -> Assistant:
    assistant = Assistant(
        id=_id,
        name=name,
        instructions=instructions,
        model=model,
        tools=tools,
        user=user,
    )
    await assistant.create()
    return assistant


async def list_assistants_by_user(user_id: PydanticObjectId) -> List[Assistant]:
    return await Assistant.find(Assistant.user.id == user_id).to_list()


async def get_assistant(_id: str) -> Optional[Assistant]:
    if _id is None:
        return None
    return await Assistant.get(_id)
