# -*- coding: utf-8 -*
# @Time : 2020/12/3 9:11
import time

from sqlalchemy.orm import Session

from app.common.deps import get_db
from app.db.session import SessionLocal
from app.models.spider import Tasks,CustomizedTasks


db: Session = SessionLocal()


def start_spider_status(taskId):
    taskInfo = db.query(Tasks).filter(Tasks.task_id == taskId).first()
    try:
        taskInfo.task_status = 0
        taskInfo.last_run_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        db.commit()
        return {'status_code': 200, 'message': '状态更新成功'}
    except:
        print("产生数据库回滚 ！！！")
        db.rollback()


def end_spider_status(taskId, spiderStatus=1):
    taskInfo = db.query(Tasks).filter(Tasks.task_id == taskId).first()
    try:
        taskInfo.task_status = 1
        taskInfo.last_run_status = spiderStatus
        taskInfo.last_run_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        db.commit()
        return {'status_code': 200, 'message': '状态更新成功'}
    except:
        print("产生数据库回滚 ！！！")
        db.rollback()


def get_spider_status(taskId):
    taskInfo = db.query(Tasks).filter(Tasks.task_id == taskId).first()
    try:
        return {'status_code': 200, 'message': '获取状态成功', 'data': taskInfo.task_status}
    except:
        print("产生数据库回滚 ！！！")
        db.rollback()
        return {'status_code': 306, 'message': 'ID不存在，我也帮不了你'}
