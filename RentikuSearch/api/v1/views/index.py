from fastapi import APIRouter

router = APIRouter(prefix="/api/v1")


@router.get("/status")
def get_status():
    return {"status": "Alive"}
