from fastapi import APIRouter

generic_router = APIRouter()


@generic_router.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}
