from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.requests import Request

from app.db.mongo_curl import do_info
from app.db.mongo_db import get_database
from app.db.redis_curl import RedisQueue

router = APIRouter()


# redis参数
def redis_param(
        *, request: Request,

):
    info = RedisQueue().info()
    # print(info)
    return {"code": 20000, "data": info}


# mongodb参数
async def mongo_param(
        *, request: Request,
        db: AsyncIOMotorClient = Depends(get_database),

):
    mongo_info = await do_info(db)
    return {"code": 20000, "data": mongo_info}


router.add_api_route(methods=['GET'], path="/redis", endpoint=redis_param, summary="redis 参数")
router.add_api_route(methods=['GET'], path="/mongo", endpoint=mongo_param, summary="mongodb 参数")
