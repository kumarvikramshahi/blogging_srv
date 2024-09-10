from pydantic import BaseModel, Field
from typing import Any
from enum import Enum


class GenericResponse(BaseModel):
    Data: Any = Field(alias="data")


class ErrorCode(str, Enum):
    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"
    BAD_REQUEST = "BAD_REQUEST"


class ErrorResponse(BaseModel):
    Code: ErrorCode = Field(alias="code")
    Message: str = Field(alias="message")
