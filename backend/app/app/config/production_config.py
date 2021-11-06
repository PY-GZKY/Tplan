#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from typing import List, Union, Optional
from urllib import parse

from pydantic import AnyHttpUrl, BaseSettings, EmailStr, validator, PostgresDsn


class Settings(BaseSettings):
    """
    线上环境配置
    """
    DEBUG: bool = True
    PROFILER_ON: bool = 0
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "(-ASp+_)-Ulhw0848hnvVG-iqKyJSD&*&^-H3C9mqEqSl8KN-YRzRE"

    # token过期时间 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 2

    #  根路径
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # print(BASE_DIR)

    # 项目信息
    PROJECT_NAME: str = "Tplan"
    DESCRIPTION: str = "Tplan"
    SERVER_NAME: str = "API_V1"

    # 跨域
    BACKEND_CORS_ORIGINS: List[str] = ['*']

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    # 批量调度主机最大并发数, 这里是使用线程池
    MAX_CONUT = 8

    # 是否开启节点免密登录
    NO_PASSWORD = False

    # 远程服务器任务存放目录
    REMOTE_DIR = "/home/tasks"

    # 本地服务器任务存放目录(主服务器)
    LOCAL_DIR: str = f"{BASE_DIR}/task"

    # 远程命令
    HOST_INFO_COMMAND = "inxi"
    UNZIP_COMMAND = "unzip -o {} -d {}"
    SUDO_PASSWORD_COMMAND = "echo {} | sudo -S mkdir {}"
    PYTHON_VERSION_COMMAND = "python --version"
    PIP_LIST_COMMAND = "pip --version"

    # 主节点信息 暂时只支持本地作为master节点
    # master主要作为调度器引擎,建议不要运行爬虫任务,负责提供中间队列和后端存储服务、以及信息缓存的工作
    MASTER = "master"
    MASTER_NAME = "本地 master 节点"
    MASTER_HOST = "127.0.0.1"
    MASTER_PORT = 22
    MASTER_USERNAME = "pai"
    MASTER_PASSWORD = "pai"
    MASTER_DESC = "本地 master 节点"

    # 缓存 key 一周后过期
    REDIS_CACHE_KEY = "fastapi_cache:"
    HOST_DETAIL_KEY = "host_detail:"
    HOST_CACHE_EXPIRE = 60 * 60  # 60 * 60 * 24 * 7

    # Redis配置项
    REDIS_USERNAME: str = os.getenv("REDIS_USERNAME", None)
    REDIS_PASSWORD: str = os.getenv("REDIS_PASSWORD", None)
    REDIS_HOST: str = os.getenv("REDIS_HOST", None)
    REDIS_PORT: int = os.getenv("REDIS_PORT", 6379)
    REDIS_DATABASE: int = os.getenv("REDIS_DATABASE", 15)
    REDIS_ENCODING: str = os.getenv("REDIS_ENCODING", "utf8")
    REDIS_MAX_CONNECTIONS: int = os.getenv("REDIS_MAX_CONNECTIONS", 10)
    REDIS_URI = f"redis://{REDIS_HOST}:{REDIS_PORT}"

    # MongoDB 配置项
    MAX_CONNECTIONS_COUNT = int(os.getenv("MAX_CONNECTIONS_COUNT", 10))
    MIN_CONNECTIONS_COUNT = int(os.getenv("MIN_CONNECTIONS_COUNT", 10))
    MONGODB_URL = os.getenv("MONGODB_URL", "")
    if not MONGODB_URL:
        MONGO_HOST: str = os.getenv("MONGO_HOST", None)
        MONGO_PORT: int = os.getenv("MONGO_PORT", 27017)
        MONGO_USER: str = os.getenv("MONGO_USER", None)
        MONGO_PASS: str = os.getenv("MONGO_PASS", None)
        MONGO_DB: str = os.getenv("MONGO_DB", None)
        MONGO_TABLE: str = os.getenv("MONGO_TABLE", "")
        MONGODB_URL: str = f"mongodb://{MONGO_USER}:{parse.quote_plus(MONGO_PASS)}@{MONGO_HOST}:{MONGO_PORT}"  # 如果携带账号和密码就加上

    #  MYSQL配置项
    MYSQL_USERNAME: str = os.getenv("MYSQL_USERNAME", None)
    MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD", None)
    MYSQL_HOST: str = os.getenv("MYSQL_HOST", None)
    MYSQL_PORT: int = os.getenv("MYSQL_PORT", 3306)
    MYSQL_DATABASE: str = os.getenv("MYSQL_DATABASE",None)

    # MYSQL 连接多个数据库
    DATABASE_URL = f"mysql://{MYSQL_USERNAME}:{parse.quote_plus(MYSQL_PASSWORD)}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8mb4"
    SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8"
    # SQLALCHEMY_DATABASE_URL1 = "mysql+pymysql://root:password@localhost:3306/task?charset=utf8mb4"
    # SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/crawlAdmin?charset=utf8mb4"

    # 默认生成用户数据 总得有一个默认的最高权限账户
    FIRST_SUPERUSER: str = "pai"
    FIRST_MALL: EmailStr = "admin@163.com"
    INIT_SUPERUSER_PASSWORD: str = "123"
    FIRST_ROLE: int = 999  # 超级管理员
    FIRST_AVATAR: AnyHttpUrl = "https://avatar-static.segmentfault.com/106/603/1066030767-5d396cc440024_huge256"

    class Config:
        case_sensitive = True


# 单例模式的最简写法
settings = Settings()

