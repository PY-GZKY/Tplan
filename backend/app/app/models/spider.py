import datetime
import time
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Date, DateTime, Text
from sqlalchemy.orm import relationship

from app.db.base_class import Base


# 项目表
class Project(Base):
    project_id = Column(String(50), primary_key=True, comment='项目Id')
    project_name = Column(String(50), comment='项目')
    project_desc = Column(String(528), comment='简介')
    update_time = Column(DateTime, default=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), comment='更新时间')
    tasks = relationship('Tasks', backref='project')


# 通用任务表
class Tasks(Base):
    project_id = Column(String(50), ForeignKey('project.project_id'), comment='项目Id')
    task_id = Column(String(50), primary_key=True, comment='task_id')
    task_name = Column(String(128), default='', comment='名称')
    task_desc = Column(String(528), default='', comment='描述')
    task_level = Column(String(128), default='', comment='运行频率等级')
    task_status = Column(Integer, default=1, comment='当前状态')
    local_path = Column(Text, default='/home/pai/Code/', comment='本地zip目录')
    remote_path = Column(Text, default='/home/remote_test/', comment='服务器目录')
    deployed_hosts = Column(Text, default='[]', comment='已部署主机列表')
    last_run_status = Column(Integer, default=0, comment='最后运行状态')
    last_run_time = Column(DateTime, default=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), comment='最后运行时间')
    create_time = Column(DateTime, default=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), comment='创建时间')
    spider_log = relationship('TaskLog', backref='tasks')


# 定制任务表(只支持本地主机)
class CustomizedTasks(Base):
    task_id = Column(String(50), primary_key=True, comment='task_id')
    task_name = Column(String(128), default='', comment='名称')
    task_desc = Column(String(528), default='', comment='描述')
    task_level = Column(String(128), default='', comment='运行频率等级')
    task_status = Column(Integer, default=1, comment='当前状态')
    last_run_status = Column(Integer, default=0, comment='最后运行状态')
    last_run_time = Column(DateTime, default=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), comment='最后运行时间')
    create_time = Column(DateTime, default=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), comment='创建时间')
    spider_log = relationship('CustomizedTaskLog', backref='customized_tasks')


# 任务日志表
class TaskLog(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    task_id = Column(String(50), ForeignKey('tasks.task_id'))
    host = Column(String(50), comment='主机节点')
    task_log_msg = Column(Text, comment='日志信息')
    task_log_level = Column(String(50), comment='日志等级')
    update_time = Column(String(50), default=str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())), comment='记录时间')


# 任务日志表
class CustomizedTaskLog(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    task_id = Column(String(50), ForeignKey('customized_tasks.task_id'))
    task_log_msg = Column(Text, comment='日志信息')
    task_log_level = Column(String(50), comment='日志等级')
    update_time = Column(String(50), default=str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())), comment='记录时间')
