from fastapi import APIRouter

from app.api.api_v1.router.spider import tasks


router = APIRouter()
router.include_router(tasks.router)
