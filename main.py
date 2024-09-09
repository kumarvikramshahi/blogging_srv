from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from api.routers import GenericRouters

app = FastAPI()


# exception handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content=exc.detail)


@app.get("/")
def Health():
    return "Hello from Blogging Service"


app.include_router(GenericRouters)
