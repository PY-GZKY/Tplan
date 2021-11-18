import json

from fastapi import APIRouter
from starlette.requests import Request

from app.arq.jobs import Job

router = APIRouter()


async def test(request: Request):
    job = await request.app.state.arq_redis.enqueue_job('say_hello', name="wt", _queue_name="arq:queue")
    job_ = await job.info()
    return {"job_": job_}


async def index(request: Request):
    functions = await request.app.state.arq_redis.all_tasks()
    workers = await request.app.state.arq_redis.all_workers()
    results = await request.app.state.arq_redis.all_job_results()
    functions_num = len(list(functions))
    workers_num = len(list(workers))
    results_num = len(results)
    results = {"functions_num": functions_num, "workers_num": workers_num, "results_num": results_num, }
    return {"code": 20000, "results": results}


async def get_all_workers(request: Request):
    workers = await request.app.state.arq_redis.all_workers()
    results = []
    for worker in workers:
        r = await request.app.state.arq_redis._get_health_check(
            queue_name=f'{json.loads(worker).get("queue_name")}:health-check')
        if r:
            r_ = json.loads(r)
            r_.update({"is_action": json.loads(worker).get("is_action"),
                       "queue_name": json.loads(worker).get("queue_name"),
                       "worker_name": json.loads(worker).get("worker_name")})
            results.append(r_)

    return {"code": 20000, "result": results, "total": len(results)}


async def get_all_task(request: Request):
    functions = await request.app.state.arq_redis.all_tasks()
    cron_list = []
    task_list = []
    for v in functions:
        if json.loads(v).get("is_timer"):
            cron_list.append(json.loads(v))
        else:
            task_list.append(json.loads(v))
    results = {"task_list": task_list, "cron_list": cron_list, "cron_num": len(cron_list), "task_num": len(task_list)}
    return {"code": 20000, "results": results}


async def get_all_result(
        request: Request,
        queue_name="arq:queue",
        worker=None,
        task=None,
        status=None,
        job_id=None,
        start_time=None,
        end_time=None,
):
    queued_jobs_ = await request.app.state.arq_redis.queued_jobs(queue_name=queue_name)
    queued_jobs__ = []
    for queued_job_ in queued_jobs_:
        state = await Job(job_id=queued_job_.__dict__.get("job_id"), redis=request.app.state.arq_redis,
                          _queue_name=queue_name).status()
        queued_job_.__dict__.update({"state": state})
        queued_jobs__.append(queued_job_.__dict__)

    results = await request.app.state.arq_redis.all_job_results()
    results_ = []
    for result in results:
        result.__dict__.update({"state": "complete"})
        results_.append(result.__dict__)

    all_result_ = results_ + queued_jobs__
    if worker:
        all_result_ = [result_ for result_ in all_result_ if result_.get("worker_name") == worker]
    if task:
        all_result_ = [result_ for result_ in all_result_ if result_.get("function") == task]
    if job_id:
        all_result_ = [result_ for result_ in all_result_ if result_.get("job_id") == job_id]

    return {"code": 20000, "results": all_result_, "total": len(all_result_)}


router.add_api_route(methods=['GET'], path="/test", endpoint=test, summary="test")
router.add_api_route(methods=['GET'], path="/index", endpoint=index, summary="index")
router.add_api_route(methods=['GET'], path="/get_all_task", endpoint=get_all_task, summary="get_task_list")
router.add_api_route(methods=['GET'], path="/get_all_workers", endpoint=get_all_workers, summary="get_all_workers")
router.add_api_route(methods=['GET'], path="/get_all_result", endpoint=get_all_result, summary="get_all_result")
