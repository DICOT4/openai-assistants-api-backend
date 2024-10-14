from datetime import datetime
from typing import List, Optional

from beanie import Document, Link
from openai.types.beta import (
    AssistantTool,
)
from pydantic import Field

from api.db.models.user import User


class Assistant(Document):
    id: str
    name: str
    instructions: str
    model: str
    tools: Optional[List[AssistantTool]]
    user: Link[User]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
