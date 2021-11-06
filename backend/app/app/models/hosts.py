# -*- coding: utf-8 -*
# @Time : 2020/11/10 13:37


import time

from sqlalchemy import Boolean, Column, DateTime, Integer, Text, String

from app.db.base_class import Base


class Hosts(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    host_name = Column(String(50), default='', comment='名称')
    ip = Column(String(50), default='', comment='IP')
    port = Column(Integer, default=22, comment='端口')
    username = Column(String(100), default='root', comment='用户名')
    password = Column(Text, default='', comment='密码')
    host_type = Column(String(50), default="worker", comment='类型,默认工作节点')
    host_status = Column(Integer, default=0, comment='状态,是否在线')
    is_verify = Column(Boolean, default=False, comment='是否免密登录')
    uuid = Column(String(500), comment='uuid识别号')
    desc = Column(String(500), default='', comment='描述')
    update_time = Column(DateTime, default=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), comment='更新时间')
