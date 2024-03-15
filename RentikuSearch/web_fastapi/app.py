from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from RentikuSearch.web_fastapi.views import (about, index, login, property,
                                             signup)

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="RentikuSearch/web_fastapi/static"),
    name="static",
)

app.include_router(index.router)
app.include_router(login.router)
app.include_router(property.router)
app.include_router(about.router)
app.include_router(signup.router)
