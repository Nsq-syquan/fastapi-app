import uuid
from typing import Optional
from pydantic import BaseModel, Field


class RepsonseObj(BaseModel):
    errorMessage: str = Field(default="")
    object: object | list 
    error: bool = Field(default=False)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "errorMessage": "",
                "object": {},
                "error": False
            }
        }
