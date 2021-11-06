import uuid
from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: Any
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        import re
        # 如果没有指定__tablename__  则默认使用model类名转换表名字
        name_list = re.findall(r"[A-Z][a-z\d]*", cls.__name__)
        # 表名格式替换成 下划线_格式 如 MallUser 替换成 mall_user
        return "_".join(name_list).lower()

    @declared_attr
    def __table_args__(cls) -> dict:
        return {'extend_existing': True}  # 创建时跳过已创建的表

    def dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

    def list(self):
        return [getattr(self, c.name, None) for c in self.__table__.columns]


def gen_uuid() -> str:
    return uuid.uuid4().hex
