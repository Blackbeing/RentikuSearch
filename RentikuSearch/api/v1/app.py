from fastapi import FastAPI

app = FastAPI()


@app.get("/test")
async def test_page():
    return {"message": "Hello world"}
