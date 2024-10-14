from typing import List, Optional

from beanie import PydanticObjectId

from api.db.models import Thread, User


async def create_thread(_id: str, title: str, user: User) -> Thread:
    thread = Thread(id=_id, title=title, user=user)
    await thread.create()
    return thread


async def list_threads_by_user(user_id: PydanticObjectId) -> List[Thread]:
    return await Thread.find(
        Thread.user.id == user_id,
    ).to_list()


async def get_thread(_id: str) -> Optional[Thread]:
    if _id is None:
        return None
    return await Thread.get(_id)
