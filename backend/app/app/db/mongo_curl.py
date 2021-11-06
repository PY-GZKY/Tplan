# -*- coding: utf-8 -*
# @Time : 2020/12/22 17:39

from datetime import datetime
from app.config import settings
from bson import SON
from motor.motor_asyncio import AsyncIOMotorClient


# 帮助文档  https://juejin.cn/post/6844903896813404173

async def do_info(db: AsyncIOMotorClient, databaseName=settings.MONGO_DB, ):
    server_status = await db[databaseName].command("serverStatus", )
    db_stats = await db[databaseName].command("dbstats", )
    item = {}
    item["version"] = server_status.get("version")
    item["connections"] = server_status.get("connections")
    item["uptime"] = server_status.get("uptime")
    item["mem"] = server_status.get("mem")
    item["collections"] = db_stats.get("collections")
    item["objects"] = db_stats.get("objects")
    print(item)
    return item


async def do_insert(db: AsyncIOMotorClient, result: list, databaseName=settings.MONGO_DB,
                    collection=settings.MONGO_TABLE):
    result = await db[databaseName][collection].insert_many(result)  # insert_many可以插入一条或多条数据，但是必须以列表(list)的形式组织数据
    print('inserted %d docs' % (len(result.inserted_ids),))


async def do_find(db: AsyncIOMotorClient, databaseName=settings.MONGO_DB, collection=settings.MONGO_TABLE) -> list:
    l_list = []
    async for document in db[databaseName][collection].find({}, {'_id': 0}):  # 查询所有文档
        l_list.append(document)
    return l_list


async def do_find_select(db: AsyncIOMotorClient, currentPage: int, pageSize: int, databaseName=settings.MONGO_DB,
                         collection=settings.MONGO_TABLE) -> list:
    l_list = []
    async for document in db[databaseName][collection].find({}, {'_id': 0}).skip((currentPage - 1) * pageSize).limit(
            pageSize):  # 查询文档
        l_list.append(document)
    return l_list


async def do_find_select_time(db: AsyncIOMotorClient, startTime, endTime, databaseName=settings.MONGO_DB,
                              collection=settings.MONGO_TABLE) -> list:
    l_list = []
    async for document in db[databaseName][collection].find(
            {"统计日期": {"$gte": startTime, "$lt": endTime}}):  # 查询时间文档
        l_list.append(document)
    return l_list


async def do_delete_many(db: AsyncIOMotorClient, databaseName=settings.MONGO_DB, collection=settings.MONGO_TABLE):
    await db[databaseName][collection].delete_many({'i': {'$gte': 1000}})  # 批量删除


async def do_update(db: AsyncIOMotorClient, databaseName=settings.MONGO_DB, collection=settings.MONGO_TABLE):
    result = await db[databaseName][collection].update_one({'i': 51},
                                                           {'$set': {'key': 'value'}})  # 仅新增或更改该文档的某个key, 或 update
    print('updated %s document' % result.modified_count)
    new_document = await db[databaseName][collection].find_one({'i': 51})
    print('document is now %s'.format(new_document))


async def do_count(db: AsyncIOMotorClient, databaseName=settings.MONGO_DB, collection=settings.MONGO_TABLE):
    n = await db[databaseName][collection].count_documents({})  # 查询集合内所有文档数量
    print('%s documents in collection' % n)
    # n = await db[databaseName][collection].count_documents({'i': {'$gt': 1000}})  # 按条件查询集合内文档数量
    # print('%s documents where i > 1000' % n)
    return n
