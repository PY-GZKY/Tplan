from typing import Optional
from starlette.requests import Request
from starlette.responses import Response
from app import settings


def default_key_builder(
        func,
        namespace: Optional[str] = "100875",
        request: Optional[Request] = None,
        response: Optional[Response] = None,
        args: Optional[tuple] = None,
        kwargs: Optional[dict] = None,
):
    return f"{settings.REDIS_CACHE_KEY}{settings.HOST_DETAIL_KEY}{namespace}"