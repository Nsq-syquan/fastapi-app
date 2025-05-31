from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models.provincemodel import Province, ProvinceUpdate
from models.responseObj import RepsonseObj

router = APIRouter()


@router.get("/province/", response_description="List all province", response_model=RepsonseObj)
def list_provinces(request: Request):
    provinces: list[Province] = list(
        request.app.database["provinces"].find(limit=100, projection={'_id': 0}).sort("provinceid", 1))
    return RepsonseObj(
        errorMessage="",
        object=provinces,
        error=False
    )


@router.get("/province/{id}", response_description="Get a single province by id", response_model=RepsonseObj)
def find_book(id: int, request: Request):
    if (province := request.app.database["provinces"].find_one({"provinceid": id}, {'_id': 0})) is not None:
        return RepsonseObj(
            errorMessage="",
            object=province,
            error=False
        )
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Province with ID {id} not found")


@router.post("/province/update", response_description="Update a single province by id", response_model=RepsonseObj)
def find_book(item: ProvinceUpdate, request: Request):
    province = request.app.database["provinces"].find_one(
        {"provinceid": item.provinceid})
    if (province) is not None:
        newValues = {"$set": {
            "provinceid": province["provinceid"], "provincename": item.provincename, "description": item.description}}
        request.app.database["provinces"].update_one(province, newValues)

        return RepsonseObj(
            errorMessage="",
            object=item,
            error=False
        )
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Province with ID {id} not found")
