from fastapi import FastAPI

from RentikuSearch.api.v1.views import index, property, user

app = FastAPI()

app.include_router(index.router)
app.include_router(user.router)
app.include_router(property.router)


@app.get("/test")
async def test_page():
    return {"message": "Hello world"}
