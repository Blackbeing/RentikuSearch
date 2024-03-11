from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from RentikuSearch.models import crud, schemas
from RentikuSearch.models.database import get_db

router = APIRouter(prefix="/api/v1")


@router.get("/property", status_code=200)
def properties(db: Session = Depends(get_db)):
    return crud.get_properties(db=db)


@router.post(
    "/property", status_code=201, response_model=schemas.PropertyCreate
)
async def create_property(
    property: schemas.PropertyCreate, db: Session = Depends(get_db)
):
    db_property = crud.get_property_by_title(db=db, title=property.title)
    if db_property:
        raise HTTPException(status_code=409, detail="Property already exists")
    return crud.create_property(db=db, property=property)


@router.get(
    "/property/{id}", response_model=schemas.Property, status_code=200
)
def get_property_by_id(id: int, db: Session = Depends(get_db)):
    db_property = crud.get_property_by_id(db=db, id=id)
    if db_property is None:
        raise HTTPException(status_code=400, detail="Property does not exist")
    return crud.get_property_by_id(db=db, id=id)
