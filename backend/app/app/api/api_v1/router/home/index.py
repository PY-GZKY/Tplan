from typing import Any, Union

from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.requests import Request

router = APIRouter()


async def get_index(request: Request) -> Any:
    return {"code": 200}  # request.app.state.templates.TemplateResponse("index.html", {"request": request})


# ------------------------------- 路由添加 --------------------------------
# 路径 和 路由方法名统一，映射到前端
router.add_api_route(methods=['GET'], path="/",
                     endpoint=get_index, summary="vue_index")
