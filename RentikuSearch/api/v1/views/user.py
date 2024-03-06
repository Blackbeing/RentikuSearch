from fastapi import APIRouter, Request

from RentikuSearch.models import schemas, storage
from RentikuSearch.models.models import User

router = APIRouter(prefix="/api/v1")


@router.get("/user", response_model=list[schemas.User], status_code=200)
def users():
    return storage.all(User)


@router.post("/user", response_model=schemas.User, status_code=201)
async def create_user(request: Request):
    data = await request.json()
    if data:
        user = User(**data)
        user.save()
        return user


@router.get("/user/{id}", response_model=schemas.User, status_code=200)
def get_user_by_id(id: int):
    return storage.get(User, id)
