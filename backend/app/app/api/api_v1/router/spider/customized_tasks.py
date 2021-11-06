# -*- coding: utf-8 -*
# @Time : 2020/11/10 15:00
import json

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from starlette.requests import Request

from app.api.utils.responseCode import resp_200
from app.common.deps import get_db
from app.config.development_config import settings
from app.logger import logger
from app.models.spider import Project, Tasks

router = APIRouter()

# 所有任务
def task_search_list(
        *, request: Request,
        project: str = Query(None, title="项目", description="项目"),
        status: str = Query(None, title="状态", description="状态"),
        page: int = 1,
        limit: int = 10,
        db: Session = Depends(get_db)
):
    if all([project, status]):
        taskList = db.query(Tasks).filter(Tasks.project_id == project, Tasks.task_status == status).limit(limit).offset(
            (page - 1) * limit)
    elif project:
        taskList = db.query(Tasks).filter(Tasks.project_id == project).limit(limit).offset((page - 1) * limit)
    elif status:
        taskList = db.query(Tasks).filter(Tasks.task_status == status).limit(limit).offset((page - 1) * limit)
    else:
        taskList = db.query(Tasks).limit(limit).offset((page - 1) * limit)
    resultList = taskList.all()
    total = taskList.count()
    result_list = [{
        'project_id': task.project_id,
        'task_id': task.task_id,
        'task_name': task.task_name,
        'task_desc': task.task_desc,
        'task_level': task.task_level,
        'task_status': task.task_status,
        'last_run_status': task.last_run_status,
        'local_path': task.local_path,
        'last_run_time': str(task.last_run_time),
        'create_time': str(task.create_time),
    } for task in resultList]

    return resp_200(data={"data": result_list, "total": total})


# 任务详情
def task_detail(*, request: Request,
                taskId: str,
                db: Session = Depends(get_db)
                ):
    # try:
    print(taskId)
    taskInfo = db.query(Tasks).filter(Tasks.task_id == taskId).first()
    data = {
        'project_id': taskInfo.project_id,
        'task_id': taskInfo.task_id,
        'task_name': taskInfo.task_name,
        'task_desc': taskInfo.task_desc,
        'task_level': taskInfo.task_level,
        'task_status': taskInfo.task_status,
        'last_run_status': taskInfo.last_run_status,
        'task_path': settings.REMOTE_DIR,
        'deployed_host': json.loads(taskInfo.deployed_hosts) if taskInfo.deployed_hosts else [],
        'last_run_time': str(taskInfo.last_run_time),
        'create_time': str(taskInfo.create_time),

    }
    return resp_200(data=data, message='获取成功')
    # except:
    #     db.rollback()
    #     return resp_400(message='获取失败')


def run_task(
        *, request: Request,
        dict_params: dict,
        db: Session = Depends(get_db)
):
    # try:

    # start_spider_status(dict_params.get("taskId"))
    print(f"jId: {dict_params.get('jId')}")
    # Mafeng().run()
    # 更新任务状态
    # end_spider_status(dict_params.get("taskId"))

    return resp_200(data={'taskName': '马蜂窝'}, message='成功')

    # except:
    #     db.rollback()
    #     return resp_400(message='操作失败')


# ------------------------------- 路由添加 --------------------------------


router.add_api_route(methods=['GET'], path="/tasks",
                     endpoint=task_search_list, summary="返回所有任务")
router.add_api_route(
    methods=['GET'], path="/task/detail", endpoint=task_detail, summary="任务详情")
router.add_api_route(methods=['POST'], path="/task/run",
                     endpoint=run_task, summary="任务开启")
