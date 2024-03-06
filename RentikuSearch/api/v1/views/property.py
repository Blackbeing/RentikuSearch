from fastapi import APIRouter, Request

from RentikuSearch.models import schemas, storage
from RentikuSearch.models.models import Property

router = APIRouter(prefix="/api/v1")


@router.get("/property", status_code=200)
def properties():
    return storage.all(Property)


@router.post("/property", status_code=201)
async def create_property(request: Request):
    data = await request.json()
    if data:
        property = Property(**data)
        property.save()
        return property


@router.get(
    "/property/{id}", response_model=schemas.Property, status_code=200
)
def get_property_by_id(id: int):
    return storage.get(Property, id)
