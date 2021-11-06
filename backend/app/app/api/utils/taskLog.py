import time
from typing import List, Union

from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.spider import TaskLog

db: Session = SessionLocal()

"""关于命令行逐行获取输出结果我这里并没有非常好的思路"""
"""这里可以根据　web socket 做实时日志"""
"""在存数据前清空该　taskId 的日志记录,只保留最后一次"""
"""或者这里可以使用 redis 缓存,设置合理的过期时间"""


def remove_task_log(taskId: str) -> bool:
    try:
        db.query(TaskLog).filter(TaskLog.task_id == taskId).delete(synchronize_session=False)
        db.commit()
        return True
    except:
        print("产生数据库回滚")
        db.rollback()
        return False


def add_task_log(taskId: str, taskLogMsg: Union[str, dict, List[str]], host: str, taskLogLevel="DEBUG") -> bool:
    try:
        createSpiderLog = TaskLog(
            task_id=taskId,
            host=host,
            task_log_level=taskLogLevel,
            task_log_msg=taskLogMsg,
            update_time=str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        db.add(createSpiderLog)
        db.commit()
        return True
    except:
        print("产生数据库回滚")
        db.rollback()
        return False


def query_task_log(taskId) -> list:
    # try:
    taskLogList = db.query(TaskLog).filter(TaskLog.task_id == taskId).all()
    # print(task_log_list)
    loggers = []
    if len(taskLogList) > 0:
        for task in taskLogList:
            item = {
                'id': task.id,
                'taskId': task.task_id,
                'host': task.host,
                'taskLogLevel': task.task_log_level,
                'taskLogMsg': task.task_log_msg,
                'updateTime': str(task.update_time),
            }
            loggers.append(item)
        return loggers

    # except:
    #     print("LOG 数据库回滚")
    #     db.rollback()
    #     return False

# print(query_task_log("6be83f39-01c1-4cef-8b87-f9d69806e5f6"))
