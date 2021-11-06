# -*- coding: utf-8 -*-
"""
模仿Flask工厂模式
"""
import os
import sys
import time

from arq import create_pool
from arq.connections import RedisSettings
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_profiler.profiler_middleware import PyInstrumentProfilerMiddleware
from fastapi_utils.tasks import repeat_every
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.middleware.cors import CORSMiddleware

from app.db.mongo_db import db
from app.db.redis_db import RedisCore
from app.logger import logger
from app.middleware.access_middle import AccessMiddleware
# from app.rearq_.start import rearq
from app.supervisor_.core import Cesi

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from fastapi import FastAPI

from app.config import settings
from app.api.api_v1.api import api_v1_router
from app.api.api_v1.router.websocket import socket_app


def create_app():
    app = FastAPI(
        debug=settings.DEBUG,
        title=settings.PROJECT_NAME,  # 项目名称
        description=settings.DESCRIPTION,  # 项目简介
        # docs_url=f"{settings.API_V1_STR}/docs",  # 自定义 docs文档的访问路径
        # openapi_url=f"{settings.API_V1_STR}/openapi.json"
    )

    # 中间件
    register_middleware(app)

    # 注册 arq
    register_arq(app)

    # 注册redis
    register_redis(app)

    # 注册mysql
    register_mysql(app)

    # 注册mongodb
    register_mongodb(app)

    # register_sup
    register_sup(app)

    # 跨域设置
    register_cors(app)

    # 注册路由
    register_router(app)

    # 尝试一个定时任务
    # register_task(app)

    # 静态文件
    # register_static_file(app)

    register_socket_io(app)

    return app


def register_middleware(app: FastAPI):
    app.add_middleware(AccessMiddleware)
    if settings.PROFILER_ON:
        app.add_middleware(PyInstrumentProfilerMiddleware, server_app=app, )
        # app.add_middleware(CProfileMiddleware, enable=True, server_app = app, filename='./output.pstats', strip_dirs = False, sort_by='cumulative')


def register_task(app: FastAPI):
    # 尝试写一个定时任务
    @app.on_event("startup")
    @repeat_every(seconds=10)  # 1 hour
    async def con_task() -> None:
        logger.debug(f'你好 定时任务启动 {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}!')


def register_arq(app: FastAPI):
    @app.on_event("startup")
    async def startup():
        app.state.arq_redis = await create_pool(
            RedisSettings(
                host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                database=0,
                password=settings.REDIS_PASSWORD
            )
        )
        logger.debug("ARQ 初始化成功 ... DONE")

    @app.on_event('shutdown')
    async def shutdown():
        await app.state.arq_redis.close()


def register_redis(app: FastAPI):
    @app.on_event("startup")
    async def startup():
        redis = await RedisCore().get_redis_pool()
        # 先挂上 对象
        app.state.redis = redis

        # 初始化缓存 FastAPICache
        FastAPICache.init(RedisBackend(redis), prefix=settings.REDIS_CACHE_KEY)
        logger.debug("REDIS 数据库初始化成功 ... DONE")

    @app.on_event('shutdown')
    async def shutdown():
        app.state.redis.close()
        await app.state.redis.wait_closed()


def register_mysql(app: FastAPI):
    @app.on_event("startup")
    async def connect_to_mysql():
        logger.debug("MYSQL 数据库初始化成功 ... DONE")


def register_mongodb(app: FastAPI):
    @app.on_event("startup")
    async def connect_to_mongo():
        try:
            db.client = AsyncIOMotorClient(settings.MONGODB_URL,
                                           maxPoolSize=settings.MAX_CONNECTIONS_COUNT,
                                           minPoolSize=settings.MIN_CONNECTIONS_COUNT)

            logger.debug("MONGODB 数据库初始化成功 ... DONE")
        except:
            logger.error("MONGODB 数据库初始化失败 ... DONE")

    @app.on_event("shutdown")
    async def close_mongo_connection():
        logger.debug("MONGODB 数据库连接关闭 ... DONE")


def register_cors(app: FastAPI):
    """
    支持跨域
    :param app:
    :return:
    """
    if settings.BACKEND_CORS_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=settings.BACKEND_CORS_ORIGINS,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )


def register_sup(app: FastAPI):
    @app.on_event("startup")
    async def init_sup():
        app.state.cesi = Cesi(config_file_path="app/supervisor_/defaults/cesi.conf.toml")
        logger.debug("Supervisor 初始化成功 ... DONE")


def register_router(app: FastAPI):
    """
    :param app:
    :return:
    """
    app.include_router(
        api_v1_router,
        # prefix=settings.API_V1_STR  # 前缀
    )


def register_socket_io(app: FastAPI) -> None:
    app.mount('/', socket_app)

# todo vue 静态文件
# def register_static_file(app: FastAPI) -> None:
#     from fastapi.staticfiles import StaticFiles
#     app.mount("/static", StaticFiles(directory="./dist/static"), name="static")
#     from starlette.templating import Jinja2Templates
#     # todo templates（模板）对象, 如果不喜欢 nginx 可直接访问 index.html
#     app.state.templates = Jinja2Templates(directory="./dist")
