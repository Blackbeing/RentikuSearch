from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from RentikuSearch.web_fastapi.views import index

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="RentikuSearch/web_fastapi/static"),
    name="static",
)

app.include_router(index.router)
