from typing import Iterable, Optional

from openai.types.beta import AssistantToolParam
from pydantic import BaseModel


class AssistantInputDTO(BaseModel):
    name: str
    instructions: str
    model: str
    tools: Optional[Iterable[AssistantToolParam]]
