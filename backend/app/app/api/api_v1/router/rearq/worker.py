# import json
# import os
# import aiofiles
# from fastapi import APIRouter, Depends
# from rearq import constants, ReArq
# from rearq.server.models import JobResult
# from rearq.utils import ms_to_datetime
# from starlette.requests import Request
# from tortoise import timezone
# from tortoise.functions import Count
# from app.api.depends.depends_ import get_pager, get_rearq
# from app.api.utils.serializeObj import serialize_sqlalchemy_obj
#
# router = APIRouter()
#
#
# async def get_workers(request: Request, rearq: ReArq = Depends(get_rearq), ):
#     redis = rearq.redis
#     workers_info = await redis.hgetall(constants.WORKER_KEY)
#     workers = []
#     for worker_name, value in workers_info.items():
#         job_stat = (
#             await JobResult.filter(worker=worker_name)
#                 .annotate(count=Count("job_id"))
#                 .group_by("job__status")
#                 .values(
#                 "count",
#                 status="job__status",
#             )
#         )
#         item = {"name": worker_name, "job_stat": {job["status"]: job["count"] for job in job_stat}}
#         item.update(json.loads(value))
#         time = ms_to_datetime(item["ms"])
#         item["time"] = time
#         item["is_online"] = (timezone.now() - time).seconds <= constants.WORKER_HEARTBEAT_SECONDS + 10
#         workers.append(item)
#     return {"code": 20000, "page_title": "worker", "workers": workers}
#
#
# async def delete_worker(request: Request, rearq: ReArq = Depends(get_rearq), name: str = ""):
#     redis = rearq.redis
#     del_result = await redis.hdel(constants.WORKER_KEY, name)
#     return {"code": 20000, "data": del_result}
#
#
# async def logs(request: Request, rearq: ReArq = Depends(get_rearq), name: str = "pai"):
#     log_file = os.path.join(constants.BASE_DIR, "logs", f"worker-{name}.log")
#     async with aiofiles.open(log_file, mode="r") as f:
#         content = await f.read()
#     return {"code": 20000, "content": content}
#
#
# async def keys(request: Request, rearq: ReArq = Depends(get_rearq)):
#     workers_info = await rearq.redis.hgetall(constants.WORKER_KEY)
#     return {
#         "code": 20000,
#         "page_title": "worker info",
#         "tasks": list(rearq.task_map.keys()),
#         "workers": list(workers_info.keys()),
#     }
#
#
# router.add_api_route(methods=['GET'], path="s", endpoint=get_workers, summary="获取 worker 列表")
# router.add_api_route(methods=['GET'], path="/delete", endpoint=delete_worker, summary="删除 worker")
# router.add_api_route(methods=['GET'], path="/logs", endpoint=logs, summary="获取 worker 日志")
# router.add_api_route(methods=['GET'], path="/keys", endpoint=keys, summary="获取 worker keys")
