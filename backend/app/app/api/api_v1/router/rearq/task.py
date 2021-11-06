# import arrow
# from fastapi import APIRouter, Depends
# from starlette.requests import Request
#
# from rearq import CronTask, ReArq
# from app.api.depends.depends_ import get_rearq
# from rearq.server.models import JobResult
# from rearq.utils import ms_to_datetime
#
# router = APIRouter()
#
#
# async def get_tasks(request: Request, rearq: ReArq = Depends(get_rearq)):
#     task_map = rearq.task_map
#     tasks = []
#     cron_tasks = []
#     for task_name, task in task_map.items():
#         item = {
#             "name": task_name,
#             "queue": task.queue,
#         }
#         job_result = await JobResult.filter(job__task=task_name).order_by("-id").first()
#         if job_result:
#             item["last_time"] = arrow.get(job_result.finish_time).to('Asia/Shanghai').format('YYYY-MM-DD HH:mm:ss')
#             item["last_status"] = job_result.success
#         else:
#             item["last_time"] = None
#         if isinstance(task, CronTask):
#             item["cron"] = task.cron
#             task.set_next()
#             item["next_time"] = arrow.get(ms_to_datetime(task.next_run)).to('Asia/Shanghai').format('YYYY-MM-DD HH:mm:ss')
#             cron_tasks.append(item)
#         else:
#             tasks.append(item)
#     return {"code": 20000, "page_title": "task", "tasks": tasks, "cron_tasks": cron_tasks}
#
#
# router.add_api_route(methods=['GET'], path="s", endpoint=get_tasks, summary="获取 task 列表")
