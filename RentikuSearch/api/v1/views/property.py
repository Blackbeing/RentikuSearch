from fastapi import APIRouter, Request

from RentikuSearch.models import storage
from RentikuSearch.models.models import Property

router = APIRouter(prefix="/api/v1")


@router.get("/property/{id}", status_code=200)
def get_property_by_id(id: int):
    return storage.get(Property, id)


@router.get("/property", status_code=200)
def properties():
    return [property.to_dict() for property in storage.all(Property)]


@router.post("/property", status_code=201)
async def create_property(request: Request):
    data = await request.json()
    if data:
        property = Property(**data)
        property.save()
        return property.to_dict()
