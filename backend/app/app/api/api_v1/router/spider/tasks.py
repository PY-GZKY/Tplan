# -*- coding: utf-8 -*
# @Time : 2020/11/10 15:00
import json
import time
import uuid

import requests
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from starlette.requests import Request

from app.api.utils.responseCode import resp_200, resp_400
from app.common.deps import get_db
from app.config.development_config import settings
from app.logger import logger
from app.models.spider import Project, TaskLog, Tasks

router = APIRouter()


# 项目首页
async def project_list(*, request: Request, db: Session = Depends(get_db), ):
    # logger.info(f"用户{token_data.sub} 正在操作")
    logger.info(request.client.host)
    project_list = db.query(Project).all()
    data = [{
        'project_name': projectCore.project_name,
        'project_id': projectCore.project_id,
        'update_time': str(projectCore.update_time),
        'project_desc': projectCore.project_desc
    } for projectCore in project_list]
    return resp_200(data=data)


# 创建项目
def create_project(*, request: Request,
                   dictParam: dict,
                   db: Session = Depends(get_db)
                   ):
    try:
        createProject = Project(
            project_id=str(uuid.uuid4()),
            project_name=dictParam.get("projectName"),
            project_desc=dictParam.get("projectDesc")
        )
        db.add(createProject)
        db.commit()
        return resp_200(message='创建成功')
    except:
        db.rollback()
        return resp_400(message='创建失败')


# 删除项目
def delete_project(*, request: Request,
                   dictParam: dict,
                   db: Session = Depends(get_db)
                   ):
    try:
        # 先删除该项目下的所有任务(主键关联)
        db.query(Tasks).filter(Tasks.project_id == dictParam.get(
            "proId")).delete(synchronize_session=False)
        # 删除该项目
        db.query(Project).filter(Project.project_id == dictParam.get(
            "proId")).delete(synchronize_session=False)
        db.commit()
        return resp_200(message='删除成功')
    except:
        db.rollback()
        return resp_400(message='删除失败')


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


# 项目下任务列表
def task_list(*, request: Request,
              db: Session = Depends(get_db),
              projectId: str
              ):
    print(projectId)
    taskList = db.query(Tasks).filter(Tasks.project_id == projectId).all()
    data = [{
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
    } for task in taskList]
    return resp_200(data=data)


# 创建任务
def create_task(*, request: Request,
                dictParam: dict,
                db: Session = Depends(get_db)
                ):
    # try:
    createTask = Tasks(
        project_id=dictParam.get("projectId"),
        task_id=str(uuid.uuid4()),
        task_name=dictParam.get("taskName"),
        task_level=dictParam.get("taskLevel"),
        task_desc=dictParam.get("taskDesc"),
        local_path=dictParam.get("taskPath"),
    )
    db.add(createTask)
    db.commit()
    return resp_200(message='添加成功')
    # except:
    #     db.rollback()
    #     return resp_400(message='添加失败')


# 删除任务
def delete_task(*, request: Request,
                dictParam: dict,
                db: Session = Depends(get_db)
                ):
    print(dictParam)
    # try:
    # 先删除该任务日志信息(主键关联)
    db.query(TaskLog).filter(TaskLog.task_id == dictParam.get(
        "taskId")).delete(synchronize_session=False)
    # 删除该任务
    db.query(Tasks).filter(Tasks.task_id == dictParam.get(
        "taskId")).delete(synchronize_session=False)
    db.commit()
    return resp_200(message='删除成功')
    # except:
    #     db.rollback()
    #     return resp_400(message='删除失败')


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
        dictParam: dict,
        db: Session = Depends(get_db)
):
    # try:


    # start_spider_status(dictParam.get("taskId"))
    print(f"jId: {dictParam.get('jId')}")
    # Meituan(poiId=dictParam.get('jId')).run()
    # 更新任务状态
    # end_spider_status(dictParam.get("taskId"))

    return # resp_200(data={'task_name': 'xxx'}, message='成功')

    # except:
    #     db.rollback()
    #     return resp_400(message='操作失败')

# ------------------------------- 路由添加 --------------------------------

router.add_api_route(methods=['GET'], path="/projects",
                     endpoint=project_list, summary="返回项目列表")
router.add_api_route(
    methods=['POST'], path="/project/create", endpoint=create_project, summary="创建项目")
router.add_api_route(
    methods=['DELETE'], path="/project/delete", endpoint=delete_project, summary="删除项目")
router.add_api_route(methods=['GET'], path="/project",
                     endpoint=task_list, summary="返回项目任务列表")

router.add_api_route(methods=['GET'], path="/tasks",
                     endpoint=task_search_list, summary="返回所有任务")
router.add_api_route(
    methods=['POST'], path="/task/create", endpoint=create_task, summary="创建任务")
router.add_api_route(
    methods=['DELETE'], path="/task/delete", endpoint=delete_task, summary="删除任务")
router.add_api_route(
    methods=['GET'], path="/task/detail", endpoint=task_detail, summary="任务详情")
router.add_api_route(methods=['POST'], path="/task/run",
                     endpoint=run_task, summary="任务开启")