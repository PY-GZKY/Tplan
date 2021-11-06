from fastapi import APIRouter
from app.api.api_v1.router.system import user, department, menu, dict

router = APIRouter()
router.include_router(user.router, prefix="/system/user", )
router.include_router(menu.router, prefix="/system/menu", )
router.include_router(dict.router, prefix="/system/dict", )
router.include_router(department.router, prefix="/system/department",)

