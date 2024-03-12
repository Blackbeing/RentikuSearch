from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from RentikuSearch import dependancies as dp
from RentikuSearch.models import models, schemas


def create_user(db: Session, user: schemas.UserCreate):
    hashed_pwd = dp.hash_password(user.password)
    db_user = models.User(
        email=user.email, username=user.username, password=hashed_pwd
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_id(db: Session, id: int) -> models.User | None:
    return db.query(models.User).filter_by(id=id).first()


def get_user_by_email(db: Session, email: str) -> models.User | None:
    return db.query(models.User).filter_by(email=email).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter_by(username=username).first()


def get_users(db: Session, skip: int = 0, limit: int = 50):
    return db.query(models.User).offset(skip).limit(limit).all()


def update_user(
    db: Session, user: schemas.User, update_data: schemas.UserUpdate
):
    user.password = dp.hash_password(update_data.password)
    db.commit()
    db.refresh(user)
    return user


def delete_user_by_id(db: Session, id: int):
    user = get_user_by_id(id=id)
    if user:
        db.delete(user)
        db.commit()


def create_property(db: Session, property: schemas.PropertyCreate):
    db_property = models.Property(**property.model_dump())
    db.add(db_property)
    db.commit()
    db.refresh(db_property)
    return db_property


def get_property_by_id(db: Session, id: int) -> models.Property | None:
    return db.query(models.Property).filter_by(id=id).first()


def get_property_by_title(db: Session, title: str) -> models.Property | None:
    return db.query(models.Property).filter_by(title=title).first()


def get_properties(db: Session, skip: int = 0, limit: int = 50):
    return db.query(models.Property).offset(skip).limit(limit).all()


def update_property(
    db: Session,
    property: models.Property,
    update_data: schemas.PropertyUpdate,
):

    property_data = schemas.PropertyUpdate(**jsonable_encoder(property))
    update_data_dict = update_data.dict(exclude_unset=True)

    updated_property = property_data.copy(update=update_data_dict)
    for k, v in updated_property.model_dump().items():
        setattr(property, k, v)
    db.commit()
    db.refresh(property)
    return property


def delete_property_by_id(db: Session, id):
    property = get_property_by_id(db=db, id=id)
    if property:
        db.delete(property)
        db.commit()
