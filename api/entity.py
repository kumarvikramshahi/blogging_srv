from pydantic import BaseModel, Field
from typing import Any


class SearchBlogRequest(BaseModel):
    Query: str = Field(alias="query")


class SearchBlogResponse(BaseModel):
    Result: dict = Field(alias="result")


class AddBlogRequest(BaseModel):
    BlogTitle: str = Field(alias="blog_title")
    BlogText: str = Field(alias="blog_text")
    UserId: str = Field(alias="user_id")


class SaveBlogRequest(BaseModel):
    BlogTitle: str = Field(alias="blog_title")
    BlogText: str = Field(alias="blog_text")
    UserId: str = Field(alias="user_id")
