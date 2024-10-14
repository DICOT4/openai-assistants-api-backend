from http import HTTPStatus
from typing import Generic, List, Optional, TypeVar

from pydantic import BaseModel

M = TypeVar("M", bound=BaseModel)


class BaseGenericResponse(BaseModel):
    message: str = HTTPStatus.OK.phrase


class GenericSingleResponse(BaseGenericResponse, Generic[M]):
    data: Optional[M] = None


class GenericMultipleResponse(BaseGenericResponse, Generic[M]):
    data: Optional[List[M]]
