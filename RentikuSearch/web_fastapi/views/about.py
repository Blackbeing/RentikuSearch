from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="RentikuSearch/web_fastapi/templates")


@router.get("/about")
async def about(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("about.html", context=context)
