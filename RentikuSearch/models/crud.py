from passlib.context import CryptContext
from sqlalchemy.orm import Session

from RentikuSearch.models import models, schemas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_pwd(password: str) -> str:
    return pwd_context.hash(password)


def create_user(db: Session, user: schemas.UserCreate):
    hashed_pwd = hash_pwd(user.password)
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


def create_property(db: Session, property: schemas.PropertyCreate):
    db_property = models.Property(**property.dict())
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
