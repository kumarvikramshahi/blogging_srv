from pydantic import BaseModel, Field
from fastapi.encoders import jsonable_encoder
from core import ElasticConnection
from utils import Utils
from schemas.schema import BlogsDTO, SearchResultDTO


class BlogsModel(BaseModel):
    BlogTitle: str = Field(alias="blog_title")
    BlogText: str = Field(alias="blog_text")
    Author: str = Field(alias="author")
    Length: int = Field(alias="length")
    CreatedAt: int = Field(alias="created_at")
    UpdatedAt: int = Field(alias="updated_at")


class Blogs:
    _blogsIndex: str = None

    def __init__(self) -> None:
        self._blogsIndex = "blogs"

    async def Create(self, insertData: BlogsDTO):
        insertData.CreatedAt = Utils.currentUtcEpochTimestamp()
        insertData.UpdatedAt = Utils.currentUtcEpochTimestamp()
        encodedInsertData = jsonable_encoder(
            obj=BlogsModel(
                blog_title=insertData.BlogTitle,
                blog_text=insertData.BlogText,
                author=insertData.Author,
                length=insertData.Length,
                created_at=insertData.CreatedAt,
                updated_at=insertData.UpdatedAt,
            ),
            exclude_none=True,
        )
        result = await ElasticConnection.ElasticClient.index(
            index=self._blogsIndex, document=encodedInsertData
        )
        return result

    async def Search(self, query: dict) -> list[SearchResultDTO]:
        searchResult = await ElasticConnection.ElasticClient.search(
            index=self._blogsIndex, body=query
        )
        response: list[SearchResultDTO] = []
        for item in searchResult["hits"]["hits"]:
            response.append(
                SearchResultDTO(
                    id=item["_id"], score=item["_score"], data=item["_source"]
                )
            )
        return response
    
