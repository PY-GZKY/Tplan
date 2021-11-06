from fastapi import APIRouter
from starlette.requests import Request

from app.api.utils.responseCode import resp_200

router = APIRouter()


def get_environments(*, request: Request):
    items = {"environments": request.app.state.cesi.serialize_environments()}
    return resp_200(data=items)


# ------------------------------- 路由添加 --------------------------------
router.add_api_route(methods=['GET'], path="/environments",
                     endpoint=get_environments, summary="supervisor 获取所有 environments")
