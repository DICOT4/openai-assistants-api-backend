"""api models."""

from typing import Sequence, Type

from beanie import Document

from api.db.models.assistant import Assistant
from api.db.models.message import Message
from api.db.models.thread import Thread
from api.db.models.user import User


def load_all_models() -> Sequence[Type[Document]]:
    """Load all models from this folder."""
    return [User, Assistant, Thread, Message]
