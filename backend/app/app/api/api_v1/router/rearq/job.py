# from typing import Optional
#
# from fastapi import APIRouter, Depends, HTTPException
# from starlette.requests import Request
# from starlette.status import HTTP_404_NOT_FOUND, HTTP_409_CONFLICT
# from rearq import ReArq, constants
# from rearq.job import JobStatus
# from app.api.depends.depends_ import get_rearq, get_pager
# from rearq.server.models import Job, JobResult
# from rearq.server.responses import JobListOut, JobOut
# from rearq.server.schemas import AddJobIn, UpdateJobIn
#
# router = APIRouter()
#
#
# async def get_jobs(
#         task: Optional[str] = None,
#         job_id: Optional[str] = None,
#         start_time: Optional[str] = None,
#         end_time: Optional[str] = None,
#         status: Optional[str] = None,
#         page: Optional[int] = None,
#         limit: Optional[int] = None,
# ):
#     qs = Job.all()
#     if task:
#         qs = qs.filter(task=task)
#     if job_id:
#         qs = qs.filter(job_id=job_id)
#     if start_time:
#         qs = qs.filter(enqueue_time__gte=start_time)
#     if end_time:
#         qs = qs.filter(enqueue_time__lte=end_time)
#     if status:
#         qs = qs.filter(status=status)
#     results = await qs.limit(limit).offset(page)
#     return {"rows": results, "total": await qs.count()}
#
#
# async def get_job_result(job_id: Optional[int] = 30):
#     return await JobResult.get_or_none(job_id=job_id)
#
#
# async def update_job(update_job_in: UpdateJobIn):
#     job = await Job.get_or_none(job_id=update_job_in.job_id)
#     if not job:
#         raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Can't find job")
#     if job.status in [JobStatus.queued, JobStatus.deferred]:
#         await job.update_from_dict(update_job_in.dict(exclude_unset=True)).save()
#     else:
#         raise HTTPException(status_code=HTTP_409_CONFLICT, detail="Can't update job")
#
#
# async def delete_job(ids: str):
#     return await Job.filter(id__in=ids.split(",")).delete()
#
#
# """
# {
#   "task": "",
#   "args": [
#     10,90
#   ],
#   "kwargs": {},
#   "job_id": "",
#   "job_retry": 1
# }
# """
#
#
# async def add_job(request: Request, add_job_in: AddJobIn, rearq: ReArq = Depends(get_rearq), ):
#     task = rearq.task_map.get(add_job_in.task)
#     print("now task: ", add_job_in.task)
#     if not task:
#         raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No such task")
#     job = await task.delay(**add_job_in.dict(exclude={"task"}))
#     return {"job": job, "code": 20000}
#
#
# router.add_api_route(methods=['GET'], path="s",
#                      endpoint=get_jobs, response_model=JobListOut, summary="获取 job 列表")
#
# router.add_api_route(methods=['GET'], path="/result",
#                      endpoint=get_job_result, summary="获取 job 结果")
#
# router.add_api_route(methods=['PUT'], path="/update",
#                      endpoint=update_job, summary="更新 job")
#
# # router.add_api_route(methods=['DELETE'], path="/delete",
# #                      endpoint=delete_job, summary="删除 job")
#
# router.add_api_route(methods=['POST'], path="/add",
#                      endpoint=add_job, summary="生产 job")
