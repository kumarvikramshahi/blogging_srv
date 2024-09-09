from fastapi import APIRouter
from schemas.schema import GenericResponse
from api.entity import SearchBlogRequest, SearchBlogResponse

Router = APIRouter()


@Router.get("/search_blog", response_model=GenericResponse)
async def SearchBlog(requestItem: SearchBlogRequest):
    print(requestItem)
    responseData = GenericResponse(data=SearchBlogResponse(result={}))
    return responseData
