from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from RentikuSearch import dependancies as dp
from RentikuSearch.models import crud, schemas
from RentikuSearch.models.database import get_db

router = APIRouter(prefix="/api/v1")


@router.get("/user", response_model=list[schemas.User], status_code=200)
def users(db: Session = Depends(get_db)):
    return crud.get_users(db=db)


@router.post("/user", status_code=201, response_model=schemas.User)
async def create_user(
    user: schemas.UserCreate,
    response_model=schemas.User,
    db: Session = Depends(get_db),
):
    db_user = crud.get_user_by_username(db=db, username=user.username)
    if db_user:
        raise HTTPException(status_code=409, detail="User already exists")
    return crud.create_user(db=db, user=user)


@router.get("/user/{id}", status_code=200, response_model=schemas.User)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db=db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/user/login")
async def login_user(
    form_data: schemas.UserLogin, db: Session = Depends(get_db)
):
    token = await dp.login_for_access_token(db=db, form_data=form_data)
    return token


@router.put("/user/{id}", response_model=schemas.User)
def update_user(
    id: int, update_data: schemas.UserUpdate, db: Session = Depends(get_db)
):
    db_user = crud.get_user_by_id(db=db, id=id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    if not update_data.password:
        raise HTTPException(status_code=400, detail="Password is required")
    return crud.update_user(db=db, user=db_user, update_data=update_data)


@router.delete("/user/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    # TODO backrefs to orphan property when user is deleted
    user = crud.get_user_by_id(db=db, id=id)
    if user:
        db.delete(user)
        db.commit()
