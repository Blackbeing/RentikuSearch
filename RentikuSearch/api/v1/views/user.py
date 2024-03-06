from fastapi import APIRouter, Request

from RentikuSearch.models import storage
from RentikuSearch.models.models import User

router = APIRouter(prefix="/api/v1")


@router.post("/user", status_code=201)
async def create_user(request: Request):
    data = await request.json()
    if data:
        user = User(**data)
        user.save()
    return user.to_dict()


@router.get("/user", status_code=200)
def users():
    return [user.to_dict() for user in storage.all(User)]


@router.get("/user/{id}", status_code=200)
def get_user_by_id(id: int):
    return storage.get(User, id).to_dict()
