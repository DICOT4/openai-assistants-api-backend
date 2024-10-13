"""api models."""

from typing import Sequence, Type

from beanie import Document

from api.db.models.dummy_model import Dummy
from api.db.models.user import User


def load_all_models() -> Sequence[Type[Document]]:
    """Load all models from this folder."""
    return [Dummy, User]
