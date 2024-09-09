from fastapi import APIRouter
from api.endpoints import add_blog
from api.endpoints import search_blog

GenericRouters = APIRouter(prefix="/blogging/v1")

GenericRouters.include_router(add_blog.Router)
GenericRouters.include_router(search_blog.Router)
