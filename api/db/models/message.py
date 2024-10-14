from datetime import datetime
from typing import Literal

from beanie import Document, Link
from pydantic import Field

from api.db.models import Assistant, Thread


class Message(Document):
    id: str
    content: str
    role: Literal["user", "assistant"]
    thread: Link[Thread]
    assistant: Link[Assistant]
    timestamp: datetime = Field(default_factory=datetime.utcnow)
