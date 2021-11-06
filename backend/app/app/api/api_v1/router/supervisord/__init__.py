from fastapi import APIRouter

from app.api.api_v1.router.supervisord import nodes,environments

router = APIRouter()
router.include_router(nodes.router)
router.include_router(environments.router)
