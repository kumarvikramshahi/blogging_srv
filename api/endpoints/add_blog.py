from fastapi import APIRouter
from schemas.schema import GenericResponse
from api.entity import AddBlogRequest

Router = APIRouter()


@Router.post("/add_blog", response_model=GenericResponse)
async def AddBlog(requestItem: AddBlogRequest):
    print(requestItem)
    return "Blog added"
