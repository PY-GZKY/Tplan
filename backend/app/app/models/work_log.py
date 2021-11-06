# -*- coding: utf-8 -*
# @Time : 2020/11/10 13:37


import time

from sqlalchemy import Column, Date, DateTime, Integer, String

from app.db.base_class import Base


class Works(Base):
    __table_args__ = {'extend_existing': True}  # 创建时跳过已创建的表
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), comment='主题')
    content = Column(String(500), comment='内容')
    update_time = Column(DateTime, default=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), comment='更新时间')
    update_date = Column(Date, default=time.strftime("%Y-%m-%d", time.localtime()), comment='更新日期')
