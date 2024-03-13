from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from RentikuSearch.models import crud
from RentikuSearch.models.database import get_db

router = APIRouter()

templates = Jinja2Templates(directory="RentikuSearch/web_fastapi/templates")


@router.get("/")
def index(request: Request, db: Session = Depends(get_db)):
    properties = crud.get_properties(db, skip=0, limit=9)
    context = {"request": request, "properties": properties}
    return templates.TemplateResponse("index.html", context=context)
