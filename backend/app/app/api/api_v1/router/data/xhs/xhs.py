from typing import Any, Union

from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.requests import Request

from app import schemas
from app.api.utils.responseCode import resp_200, resp_400
from app.db.mongo_db import get_database

from app.common import deps

router = APIRouter()


async def get_xhs(
        db: AsyncIOMotorClient = Depends(get_database),
        database_name="fastapi_vue_admin",
        # token_check=Depends(deps.get_current_active_user),
        limit: int = 15,
        page: int = 1,
        title: str = '',
        content: str = '',
        username: str = '',
) -> Any:
    """mongodb-数据查询"""
    # m_db = client["小红书"]
    query_ = {"title": title, "content": content, "username": username}
    # query_ = {k:v for k,v in query_.items() if v != '' }
    query_ = {"$and": [{k: {'$regex': v} for k, v in query_.items() if v != ''}]}
    print(query_)

    # total = m_db["小红书_苏州旅游攻略"].find(query_, {"_id": 0}).count()
    # departments = m_db["小红书_苏州旅游攻略"].find(query_, {"_id": 0}).limit(limit).skip((page - 1) * limit)
    # items = [i for i in departments] 

    total = await db[database_name]["xhs_chengdu"].count_documents(query_)  # 查询所有文档
    items = [item async for item in
             db[database_name]["xhs_chengdu"].find(query_, {'_id': 0}).limit(limit).skip((page - 1) * limit)]  # 查询所有文档
    data = {"items": items, "total": total}
    return {"code": 20000, "data": data}


async def create(*, request: Request,
                 dict_params: dict,
                 db: AsyncIOMotorClient = Depends(get_database),
                 # token_check=Depends(deps.get_current_active_user),
                 database_name="fastapi_vue_admin",
                 ):
    # print(dict_params)
    try:
        return resp_200(message='添加成功')
    except:
        # 此处应有回滚操作
        return resp_400(message='添加失败')


async def update(*, request: Request,
                 dict_params: dict,
                 db: AsyncIOMotorClient = Depends(get_database),
                 # token_check=Depends(deps.get_current_active_user),
                 database_name="fastapi_vue_admin",
                 ):
    try:
        return resp_200(message='添加成功')
    except:
        # 此处应有回滚操作
        return resp_400(message='添加失败')


async def delete(*, request: Request,
                 dict_params: dict,
                 db: AsyncIOMotorClient = Depends(get_database),
                 # token_check=Depends(deps.get_current_active_user),
                 database_name="fastapi_vue_admin",
                 ):
    try:
        return resp_200(message='刪除成功')
    except:
        # 此处应有回滚操作
        return resp_400(message='添加失败')


# ------------------------------- 路由添加 --------------------------------
# 路径 和 路由方法名统一，映射到前端
router.add_api_route(methods=['GET'], path="/list", response_model=schemas.Response, endpoint=get_xhs,
                     summary="小红书")

router.add_api_route(methods=['POST'], path="/xhs/create", response_model=schemas.Response, endpoint=create,
                     summary="添加小红书评论")

router.add_api_route(methods=['PUT'], path="/xhs/update", response_model=schemas.Response, endpoint=update,
                     summary="编辑小红书评论")

router.add_api_route(methods=['DELETE'], path="/xhs/delete", response_model=schemas.Response, endpoint=delete,
                     summary="删除小红书评论")
