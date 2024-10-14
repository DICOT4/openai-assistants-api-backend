from datetime import datetime
from typing import Optional

from beanie import Document, Link
from pydantic import Field

from api.db.models.user import User


class Thread(Document):
    id: str
    title: Optional[str] = Field(default="New Conversation")
    user: Link[User]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
