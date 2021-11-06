# -*- coding: utf-8 -*
# @Time : 2020/12/22 17:29

from motor.motor_asyncio import AsyncIOMotorClient


class DataBase:
    client: AsyncIOMotorClient = None


db = DataBase()


async def get_database() -> AsyncIOMotorClient:
    return db.client
