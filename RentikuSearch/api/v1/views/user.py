from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from RentikuSearch.models import schemas
from RentikuSearch.models.database import get_db
from RentikuSearch.models.models import User

router = APIRouter(prefix="/api/v1")


@router.get("/user/{id}", status_code=200, response_model=schemas.User)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter_by(id=id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/user", response_model=list[schemas.User], status_code=200)
def users(db: Session = Depends(get_db)):
    return db.query(User).all()


@router.post("/user", status_code=201, response_model=schemas.User)
async def create_user(
    data: schemas.UserCreate,
    response_model=schemas.User,
    db: Session = Depends(get_db),
):
    user = db.query(User).filter(User.username == data.username).first()
    if user:
        raise HTTPException(status_code=409, detail="User already exists")

    user = User(**data.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    db.flush()
    return user
