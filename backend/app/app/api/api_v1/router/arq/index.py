import json

from arq.jobs import Job
from fastapi import APIRouter
from starlette.requests import Request

router = APIRouter()


async def test(request: Request):
    job = await request.app.state.arq_redis.enqueue_job('say_hello', name="wt", _queue_name="arq:queue1")
    job_ = await job.info()
    return {"job_": job_}


async def index(request: Request):
    functions = await request.app.state.arq_redis.all_tasks()
    workers = await request.app.state.arq_redis.all_workers()
    results = await request.app.state.arq_redis.all_job_results()
    functions_num = len(list(functions.keys()))
    workers_num = len(list(workers.keys()))
    results_num = len(results)
    results = {"functions_num": functions_num, "workers_num": workers_num, "results_num": results_num, }
    return {"code": 20000, "results": results}


async def get_task_list(request: Request):
    functions = await request.app.state.arq_redis.all_tasks()
    cron_list = []
    task_list = []
    for v in functions.values():
        if json.loads(v).get("is_timer"):
            cron_list.append(json.loads(v))
        else:
            task_list.append(json.loads(v))
    results = {"task_list": task_list, "cron_list": cron_list, "cron_num": len(cron_list), "task_num": len(task_list)}
    return {"code": 20000, "results": results}


async def get_all_workers(request: Request, task_name="arq:task", queue_name="arq:queue3"):
    workers = await request.app.state.arq_redis.all_workers()
    queues_ = set([json.loads(v).get("queue_name") for k, v in workers.items()])

    __ = []
    for queue_name in queues_:
        r = await request.app.state.arq_redis._get_health_check(queue_name=f"{queue_name}:health-check")
        r_ = json.loads(r)

        workers_ = [json.loads(v).get("worker_consumer_name") for k, v in workers.items() if
                    json.loads(v).get("queue_name") == queue_name]

        r_.update({"queue_name": queue_name, "workers": workers_})
        __.append(r_)

    return {"code": 20000, "result": __, "total": len(__)}


async def get_all_result(
        request: Request,
        queue_name="arq:queue1",
        worker="",
        task="",
        status="",
        job_id="",
        start_time="",
        end_time="",
):
    queued_jobs_ = await request.app.state.arq_redis.queued_jobs(queue_name=queue_name)
    queued_jobs__ = []
    for queued_job_ in queued_jobs_:
        state = await Job(
            job_id=queued_job_.__dict__.get("job_id"),
            redis=request.app.state.arq_redis,
            _queue_name=queue_name).status()

        queued_job_.__dict__.update({"state": state})
        queued_jobs__.append(queued_job_)

    results = await request.app.state.arq_redis.all_job_results()
    results_ = []
    for result in results:
        if result.__dict__.get("queue_name") == queue_name:
            result.__dict__.update({"state": "complete"})
            result.__dict__.update(
                {"expire_time": result.__dict__.get("finish_time") - result.__dict__.get("start_time")})
            results_.append(result)

    __ = results_ + queued_jobs__
    return {"code": 20000, "results": __, "total": len(__)}


router.add_api_route(methods=['GET'], path="/test", endpoint=test, summary="test")
router.add_api_route(methods=['GET'], path="/index", endpoint=index, summary="index")
router.add_api_route(methods=['GET'], path="/get_task_list", endpoint=get_task_list, summary="get_task_list")
router.add_api_route(methods=['GET'], path="/get_all_workers", endpoint=get_all_workers, summary="get_all_workers")
router.add_api_route(methods=['GET'], path="/get_all_result", endpoint=get_all_result, summary="get_all_result")
