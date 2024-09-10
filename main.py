import asyncio
from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from fastapi.responses import JSONResponse
from api.routers import GenericRouters
from kafka_streamer import KafkaProducer, KafkaConsumer


@asynccontextmanager
async def lifespan(app: FastAPI):
    await KafkaProducer.Init()
    await KafkaConsumer.Init()
    asyncio.create_task(KafkaConsumer.ConsumeMessage())
    yield  # lines above this line execute @ starup and belows @ shutdown
    await KafkaProducer.Stop()
    await KafkaConsumer.Stop()


app = FastAPI(lifespan=lifespan)


# exception handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content=exc.detail)


@app.get("/")
def Health():
    return "Hello from Blogging Service"


app.include_router(GenericRouters)
