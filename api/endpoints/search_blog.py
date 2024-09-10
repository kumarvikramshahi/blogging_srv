import logging
from elasticsearch import BadRequestError
from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder
from schemas.schema import GenericResponse, ErrorResponse, ErrorCode
from api.entity import SearchBlogRequest
from dao.blogs import Blogs

Router = APIRouter()


@Router.get("/search_blog", response_model=GenericResponse)
async def SearchBlog(requestItem: SearchBlogRequest):
    searchResult = None
    try:
        searchQuery = jsonable_encoder(requestItem)
        searchResult = await Blogs().Search(query=searchQuery)
    except (BadRequestError, Exception) as error:
        customError = ErrorResponse(
            code=ErrorCode.INTERNAL_SERVER_ERROR,
            message=f"ERROR WHILE SEARCHING BLOG IN ELASTIC DB - {str(error)}",
        )
        errStatusCode = status.HTTP_500_INTERNAL_SERVER_ERROR
        if (
            isinstance(error, BadRequestError)
            and error.status_code == status.HTTP_400_BAD_REQUEST
        ):
            customError = ErrorResponse(
                code=ErrorCode.BAD_REQUEST, message=f"{str(error)}"
            )
            errStatusCode = status.HTTP_400_BAD_REQUEST
        else:
            logging.error(f"error while querying data to elasticDB - {str(error)}")

        raise HTTPException(status_code=errStatusCode, detail=customError)

    return GenericResponse(data=searchResult)
