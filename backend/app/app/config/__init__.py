# -*- coding: utf-8 -*-
"""
配置文件
服务器上设置 ENV 环境变量
更具环境变量 区分生产开发
"""
import os

from ..logger import logger

env = os.getenv("PRODUCTION", "")
if env:
    pass
else:
    logger.debug("development 开发环境启动 .... DONE")
    from .development_config import settings
