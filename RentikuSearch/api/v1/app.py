from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from RentikuSearch.api.v1.views import index, property, user

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(index.router)
app.include_router(user.router)
app.include_router(property.router)


@app.get("/test")
async def test_page():
    return {"message": "Hello world"}
