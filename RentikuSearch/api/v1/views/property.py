from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from RentikuSearch.models import schemas
from RentikuSearch.models.database import get_db
from RentikuSearch.models.models import Property

router = APIRouter(prefix="/api/v1")


@router.get("/property", status_code=200)
def properties(db: Session = Depends(get_db)):
    return db.query(Property).all()


@router.post("/property", status_code=201, response_model=schemas.Property)
async def create_property(
    data: schemas.PropertyCreate, db: Session = Depends(get_db)
):
    if data:
        property = Property(**data.dict())
        db.add(property)
        db.commit()
        db.refresh(property)
        return property


@router.get(
    "/property/{id}", response_model=schemas.Property, status_code=200
)
def get_property_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(Property).filter_by(id=id).first()
