# # main.py
# import asyncio
# from urllib import parse
#
# from rearq import ReArq
#
# rearq = ReArq(
#     db_url=f'mysql://root:@localhost:3306/Tplan',
#     redis_host="",
#     redis_port=6379,
#     redis_password="",
#     redis_db=0,
# )
#
#
# @rearq.on_shutdown
# async def on_shutdown():
#     # you can do some clean work here like close db and so on...
#     print("shutdown")
#
#
# @rearq.on_startup
# async def on_startup():
#     # you should do some initialization work here, such tortoise-orm init and so on...
#     print("startup")
#
#
# @rearq.task(queue="my_queue")
# async def add(self, a, b):
#     return f"{a + b}"
#
#
# @rearq.task(queue="my_queue")
# async def add1(self, a, b):
#     return f"{a + b}"
#
#
#
# @rearq.task()
# async def sleep(self, time: float):
#     return await asyncio.sleep(time)
#
#
# @rearq.task(cron="0 */12 * * *")  # run task per 60 seconds
# async def timer_60(self):
#     return "timer_60"
#
#
#
#
#
