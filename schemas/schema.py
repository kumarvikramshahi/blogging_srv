from pydantic import BaseModel, Field
from typing import Any


class GenericResponse(BaseModel):
    Data: Any = Field(alias="data")
