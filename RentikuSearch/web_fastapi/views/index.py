from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from RentikuSearch.models import storage
from RentikuSearch.models.models import Property

router = APIRouter()

templates = Jinja2Templates(directory="RentikuSearch/web_fastapi/templates")


@router.get("/")
def index(request: Request):
    properties = storage.all(Property)
    return templates.TemplateResponse(
        "index.html", {"request": request, "properties": properties}
    )
