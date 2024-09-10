from fastapi import APIRouter, HTTPException, status
from schemas.schema import GenericResponse, ErrorResponse, ErrorCode
from api.entity import AddBlogRequest, SaveBlogRequest
from kafka_streamer import KafkaProducer

Router = APIRouter()


@Router.post("/add_blog", response_model=GenericResponse)
async def AddBlog(requestItem: AddBlogRequest):
    try:
        await KafkaProducer.ProduceMessage(data=requestItem)
    except HTTPException as error:
        customError = ErrorResponse(
            code=ErrorCode.INTERNAL_SERVER_ERROR, message=f"{str(error)}"
        )
        HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=customError
        )

    return GenericResponse(data={"message": "Blog added"})


@Router.post("/save_blog", response_model=GenericResponse)
async def SaveBlog(requestItem: SaveBlogRequest):
    return GenericResponse(data={"message": "Blog saved"})
