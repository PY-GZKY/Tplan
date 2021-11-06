from fastapi import APIRouter

from app.api.api_v1.router.arq import index

router = APIRouter()
router.include_router(index.router)


