from typing import Optional

from pydantic import BaseModel


class ThreadInputDTO(BaseModel):
    title: Optional[str]


class MessageInputDTO(BaseModel):
    content: str
    assistant_id: str
