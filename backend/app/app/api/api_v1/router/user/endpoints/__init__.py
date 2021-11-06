from fastapi import APIRouter

from app.api.api_v1.router.user.endpoints import login, role

router = APIRouter()
router.include_router(login.router, tags=["login"])
router.include_router(role.router, prefix="/role", tags=["role"])
