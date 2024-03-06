from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="RentikuSearch/web_fastapi/static"),
    name="static",
)
templates = Jinja2Templates(directory="RentikuSearch/web_fastapi/templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")
