# -*- coding: utf-8 -*-

import asyncio
import os

from connections import RedisSettings
from cron import cron


async def say_hello(ctx, name) -> None:
    await asyncio.sleep(30)
    print(f"Hello {name}")


async def say_hi(ctx, name) -> None:
    await asyncio.sleep(3)
    print(f"Hi {name}")


async def startup(ctx):
    print("starting...")


async def shutdown(ctx):
    print("ending...")


async def run_regularly(ctx):
    print('run job at 26:05, 27:05 and 28:05')


class WorkerSettings:
    redis_settings = RedisSettings(
        host=os.getenv("REDIS_HOST", None),
        port=os.getenv("REDIS_PORT", 6379),
        database=os.getenv("REDIS_DATABASE", 0),
        password=os.getenv("REDIS_PASSWORD", None)
    )

    functions = [say_hello, say_hi]

    on_startup = startup

    on_shutdown = shutdown

    cron_jobs = [
        cron(coroutine=run_regularly, name="x100", minute=40, second=50, keep_result_forever=True)
    ]

    allow_abort_jobs = True

    # queue_name = "arq:queue1"
