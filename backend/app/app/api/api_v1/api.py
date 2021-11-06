from app.api.api_v1.router import system, monitor, spider, host, arq, supervisord, home
from app.api.api_v1.router.data import xhs
from app.api.api_v1.router.user import endpoints
from fastapi import APIRouter

api_v1_router = APIRouter()
# 各自模块的路由由各自模块负责
api_v1_router.include_router(endpoints.router)
api_v1_router.include_router(home.router, tags=["首页"])
api_v1_router.include_router(system.router, tags=["system"])
api_v1_router.include_router(xhs.router, prefix="/xhs", tags=["xhs"])
api_v1_router.include_router(monitor.router, prefix="/monitor", tags=["数据监控"])
api_v1_router.include_router(spider.router, tags=["爬虫任务"])
api_v1_router.include_router(host.router, prefix="/host", tags=["节点"])
api_v1_router.include_router(supervisord.router, prefix="/supervisor", tags=["supervisor"])
api_v1_router.include_router(arq.router, prefix="/arq", tags=["arq"])
