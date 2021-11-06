# Import all the models, so that Base has them before being
# imported by Alembic
# imported by Alembic # 方便在Alembic导入,迁移用

'''
alembic init alembic
alembic revision --autogenerate -m "create"
alembic upgrade head
'''
