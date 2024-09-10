from fastapi import APIRouter, HTTPException, status
from schemas.schema import GenericResponse, ErrorResponse, ErrorCode, BlogsDTO
from api.entity import AddBlogRequest, SaveBlogRequest
from kafka_streamer import KafkaProducer
from dao.blogs import Blogs
import logging

Router = APIRouter()


@Router.post("/add_blog", response_model=GenericResponse)
async def AddBlog(requestItem: AddBlogRequest) -> GenericResponse:
    try:
        _ = await KafkaProducer.ProduceMessage(data=requestItem)
    except HTTPException as error:
        customError = ErrorResponse(
            code=ErrorCode.INTERNAL_SERVER_ERROR, message=f"{str(error)}"
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=customError
        )

    return GenericResponse(data={"message": "Blog added"})


@Router.post("/save_blog", response_model=GenericResponse)
async def SaveBlog(requestItem: SaveBlogRequest):
    insertData = BlogsDTO(
        blog_title=requestItem.BlogTitle,
        length=len(requestItem.BlogText),
        blog_text=requestItem.BlogText,
        author=requestItem.UserId,
    )
    # saving blog to elasticDB
    try:
        _ = await Blogs().Create(insertData=insertData)
    except Exception as error:
        logging.error(f"str{error}")
        customError = ErrorResponse(
            code=ErrorCode.INTERNAL_SERVER_ERROR,
            message="Error indexing docs in elastic",
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=customError
        )

    return GenericResponse(data={"message": "Blog saved"})
