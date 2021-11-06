# -*- coding: utf-8 -*
# @Time : 2020/11/10 15:00
from fastapi import APIRouter
from starlette.requests import Request

from app.api.utils.responseCode import resp_200, resp_400

router = APIRouter()


def get_groups_tree(*, request: Request):
    groups = request.app.state.cesi.get_groups_tree()
    data = {"items": groups}
    return resp_200(data=data)


def get_group_details(*, request: Request, group_name: str):
    groups = request.app.state.cesi.get_groups_tree()
    group = [group for group in groups if group["name"] == group_name]
    if not group:
        return resp_400()
    items = {"group": group}
    return resp_200(data=items)


def get_group_details_by_node_name(*, request: Request, group_name: str, node_name: str):
    groups = request.app.state.cesi.groups
    group = groups.get(group_name, None)
    if not group:
        return resp_400()
    if node_name not in group:
        return resp_400(message="Wrong node name for group name")
    result = {}
    n = request.app.state.cesi.get_node(node_name)
    processes = n.get_processes_by_group_name(group_name)
    result[n.name] = []
    for p in processes:
        result[n.name].append(p.serialize())
    items = {"result": result}
    return resp_200(data=items)


# ------------------------------- 路由添加 --------------------------------
router.add_api_route(methods=['GET'], path="/groups",
                     endpoint=get_groups_tree, summary="supervisor 获取所有 groups")

router.add_api_route(methods=['GET'], path="/groups/{group_name}",
                     endpoint=get_group_details, summary="supervisor 获取 group details")

router.add_api_route(methods=['GET'], path="/groups/{group_name}/node/{node_name}",
                     endpoint=get_group_details_by_node_name, summary="")
