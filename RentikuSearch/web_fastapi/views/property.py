from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from RentikuSearch.models import crud
from RentikuSearch.models.database import get_db

router = APIRouter()

templates = Jinja2Templates(directory="RentikuSearch/web_fastapi/templates")


@router.get("/properties")
def properties(request: Request, db: Session = Depends(get_db)):
    # TODO, implement pagination
    properties = crud.get_properties(db)
    context = {"request": request, "properties": properties}
    return templates.TemplateResponse("property.html", context=context)
