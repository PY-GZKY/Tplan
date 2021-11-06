# -*- coding: utf-8 -*-
# @Time : 2020-11-18 13:56

import hashlib
import json
from app.config import settings
import redis


class RedisQueue(object):

    def __init__(self, name: str = None, **redis_kwargs):
        self.pool = redis.ConnectionPool(host=settings.REDIS_HOST, username=settings.REDIS_USERNAME,
                                         password=settings.REDIS_PASSWORD, port=settings.REDIS_PORT,
                                         db=settings.REDIS_DATABASE, max_connections=settings.REDIS_MAX_CONNECTIONS)
        self.__db = redis.Redis(connection_pool=self.pool, decode_responses=True)
        self.key = name

    # 返回队列大小
    def qsize(self):
        return self.__db.llen(self.key)

    # 判断队列用尽
    def empty(self):
        return self.qsize() == 0

    def put_hash(self, key, value):
        self.__db.hset(self.key, key, value)

    def get_hash(self, key):
        return self.__db.hget(self.key, key)

    def get_all_hash(self):
        return self.__db.hkeys(self.key)

    def delete_hash(self, key):
        return self.__db.hdel(self.key, key)

    def info(self):
        redis_info = self.__db.info()
        info_item = {}
        info_item['version'] = redis_info['redis_version']
        info_item['os'] = redis_info['os']
        info_item['port'] = redis_info['tcp_port']
        info_item['used_memory_human'] = redis_info['used_memory_human']
        info_item['used_memory_peak_human'] = redis_info['used_memory_peak_human']
        return info_item
