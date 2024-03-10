from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from RentikuSearch.models.database import get_db
from RentikuSearch.models.models import Property

router = APIRouter()

templates = Jinja2Templates(directory="RentikuSearch/web_fastapi/templates")


@router.get("/")
def index(request: Request, db: Session = Depends(get_db)):
    properties = db.query(Property).all()
    return templates.TemplateResponse(
        "index.html", {"request": request, "properties": properties}
    )
