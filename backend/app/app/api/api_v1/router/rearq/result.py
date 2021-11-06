# from typing import Optional
#
# import pytz
# from fastapi import APIRouter, Depends
# from rearq.server.depends import get_pager
# from rearq.server.models import JobResult
# from rearq.server.responses import JobResultListOut
#
# router = APIRouter()
#
#
# async def get_results(
#         task: Optional[str] = None,
#         job_id: Optional[str] = None,
#         start_time: Optional[str] = None,
#         end_time: Optional[str] = None,
#         worker: Optional[str] = None,
#         success: Optional[str] = None,
#         pager=Depends(get_pager),
# ):
#     qs = JobResult.all().select_related("job")
#     if task:
#         qs = qs.filter(job__task=task)
#     if job_id:
#         qs = qs.filter(job__job_id=job_id)
#     if start_time:
#         qs = qs.filter(start_time__gte=start_time)
#     if end_time:
#         qs = qs.filter(start_time__lte=end_time)
#     if worker:
#         qs = qs.filter(worker=worker)
#     if success:
#         qs = qs.filter(success=success == 1)
#     results = await qs.limit(pager[0]).offset(pager[1])
#     return {"rows": results, "total": await qs.count(), "code": 20000}
#
#
# async def delete_result(ids: str):
#     await JobResult.filter(id__in=ids.split(",")).delete()
#     return {"code": 20000, "message": "成功"}
#
#
# router.add_api_route(methods=['GET'], path="s", endpoint=get_results, response_model=JobResultListOut, summary="所有结果集")
# router.add_api_route(methods=['DELETE'], path="/delete", endpoint=delete_result, summary="删除结果")
