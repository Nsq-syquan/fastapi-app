import uuid
from typing import Optional
from pydantic import BaseModel, Field


class Province(BaseModel):
    provinceid: int = Field(...)
    provincename: str = Field(...)
    description: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "provinceid": 1,
                "provincename": "Miguel de Cervantes",
                "description": ""
            }
        }


class ProvinceUpdate(BaseModel):
    provinceid: Optional[int]
    provincename: Optional[str]
    description: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "provinceid": 1,
                "provincename": "Miguel de Cervantes",
                "description": ""
            }
        }
