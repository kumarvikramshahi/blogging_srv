import asyncio
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from contextlib import asynccontextmanager
from fastapi.responses import JSONResponse
from api.routers import GenericRouters
from kafka_streamer import KafkaProducer, KafkaConsumer
from core import MongoConnection, ElasticConnection, logging_core


@asynccontextmanager
async def lifespan(app: FastAPI):
    # MongoConnection.Create()
    logging_core.Initialize()
    await ElasticConnection.Init()
    await KafkaProducer.Init()
    await KafkaConsumer.Init()
    asyncio.create_task(KafkaConsumer.ConsumeMessage())
    yield  # lines above this line execute @ starup and belows @ shutdown
    await KafkaProducer.Stop()
    await KafkaConsumer.Stop()
    # MongoConnection.Close()


app = FastAPI(lifespan=lifespan)


# exception handlers
@app.exception_handler(HTTPException)
def HttpExceptionHandler(request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code, content=jsonable_encoder(exc.detail)
    )


@app.get("/blogging/v1/health")
def Health():
    return "Blogging Service"


app.include_router(GenericRouters)
