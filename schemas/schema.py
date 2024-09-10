from pydantic import BaseModel, Field
from typing import Any, Optional
from enum import Enum


class GenericResponse(BaseModel):
    Data: Any = Field(alias="data")


class ErrorCode(str, Enum):
    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"
    BAD_REQUEST = "BAD_REQUEST"


class ErrorResponse(BaseModel):
    Code: ErrorCode = Field(alias="code")
    Message: str = Field(alias="message")


class BlogsDTO(BaseModel):
    Id: str = Field(alias="_id", default=None)
    BlogTitle: str = Field(alias="blog_title")
    BlogText: str = Field(alias="blog_text")
    Author: str = Field(alias="author")
    Length: int = Field(alias="length")
    CreatedAt: Optional[int] = Field(alias="created_at", default=0)
    UpdatedAt: Optional[int] = Field(alias="updated_at", default=0)


class SearchResultDTO(BaseModel):
    Id: str = Field(alias="id")
    Score: float = Field(alias="score")
    Data: dict = Field(alias="data")
