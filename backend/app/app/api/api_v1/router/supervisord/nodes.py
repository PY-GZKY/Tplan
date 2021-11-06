# -*- coding: utf-8 -*
# @Time : 2020/11/10 15:00
from fastapi import APIRouter
from starlette.requests import Request

from app.api.utils.responseCode import resp_200, resp_400, resp_500
from app.supervisor_.core.clogger import ActivityLog

router = APIRouter()
activity = ActivityLog.getInstance()


def get_nodes(*, request: Request, ):
    nodes = request.app.state.cesi.serialize_nodes()
    data = {"items": nodes, "total": len(nodes)}
    return resp_200(data=data)


def get_node(*, request: Request, node_name: str):
    node = request.app.state.cesi.get_node_or_400(node_name)
    data = {"items": node.serialize_node(), "total": len(node.serialize_node().get("processes"))}
    return resp_200(data=data)


def get_node_processes(*, request: Request, node_name: str):
    node = request.app.state.cesi.get_node_or_400(node_name)
    if not node.is_connected:
        return resp_400()
    data = {"items": node.serialize_processes()}
    return resp_200(data=data)


def get_process(*, request: Request, node_name, unique_process_name):
    node = request.app.state.cesi.get_node_or_400(node_name)
    if not node.is_connected:
        return resp_400()
    process = node.get_process_or_400(unique_process_name)
    data = {"items": process.serialize()}
    return resp_200(data=data)


def start_process(*, request: Request, node_name, unique_process_name):
    node = request.app.state.cesi.get_node_or_400(node_name)
    if not node.is_connected:
        return resp_400()
    status, msg = node.start_process(unique_process_name)
    if status:
        activity.logger.info(
            "{} started {} node's {} process.".format(
                "不知道他娘的谁", node_name, unique_process_name
            )
        )
        return resp_200(message=f"{node.name} {unique_process_name} start event successful")
    activity.logger.info(
        "{} unsuccessful start event {} node's {} process.".format("不知道他娘的谁", node_name, unique_process_name))
    return resp_500()


def stop_process(*, request: Request, node_name, unique_process_name):
    node = request.app.state.cesi.get_node_or_400(node_name)
    if not node.is_connected:
        return resp_400()
    status, msg = node.stop_process(unique_process_name)
    if status:
        activity.logger.info(
            "{} stopped {} node's {} process.".format(
                "不知道他娘的谁", node_name, unique_process_name
            )
        )
        return resp_200(message=f"{node.name} {unique_process_name} stop event successful")
    activity.logger.info(
        "{} unsuccessful stop event {} node's {} process.".format(
            "不知道他娘的谁", node_name, unique_process_name
        )
    )
    return resp_500()


def restart_process(*, request: Request, node_name, unique_process_name):
    node = request.app.state.cesi.get_node_or_400(node_name)
    if not node.is_connected:
        return resp_400()

    status, msg = node.restart_process(unique_process_name)
    if status:
        activity.logger.info(
            "{} restarted {} node's {} process.".format(
                "不知道他娘的谁", node_name, unique_process_name
            )
        )
        return resp_200(message=f"{node.name} {unique_process_name} restart event successful")

    activity.logger.info(
        "{} unsuccessful restart event {} node's {} process.".format(
            "不知道他娘的谁", node_name, unique_process_name
        )
    )
    return resp_500()


def read_process_log(*, request: Request, node_name, unique_process_name):
    node = request.app.state.cesi.get_node_or_400(node_name)
    if not node.is_connected:
        return resp_400()
    logs = node.get_process_logs(unique_process_name)
    items = {"log": logs}
    return resp_200(data=items)


# todo 这里 supervisor 实际上提供了批量操作的语句
def start_all_process(*, request: Request, node_name):
    node = request.app.state.cesi.get_node_or_400(node_name)
    if not node.is_connected:
        return resp_400()
    for process in node.processes:
        if not process.state == 20:
            status, msg = node.start_process(process.group + ":" + process.name)
            if status:
                activity.logger.info(
                    "{} started {} node's {} process.".format(
                        "不知道他娘的谁", node_name, process.name
                    )
                )
            else:

                activity.logger.info(
                    "{} unsuccessful start event {} node's {} process.".format(
                        "不知道他娘的谁", node_name, process.name
                    )
                )
    return resp_200()


def stop_all_process(*, request: Request, node_name):
    node = request.app.state.cesi.get_node_or_400(node_name)
    if not node.is_connected:
        return resp_400()
    for process in node.processes:
        if not process.state == 0:
            status, msg = node.stop_process(process.group + ":" + process.name)
            if status:

                activity.logger.info(
                    "{} stopped {} node's {} process.".format(
                        "不知道他娘的谁", node_name, process.name
                    )
                )
            else:

                activity.logger.info(
                    "{} unsuccessful stop event {} node's {} process.".format(
                        "不知道他娘的谁", node_name, process.name
                    )
                )
    return resp_200()


def restart_all_process(*, request: Request, node_name):
    node = request.app.state.cesi.get_node_or_400(node_name)
    if not node.is_connected:
        return resp_400()

    for process in node.processes:
        if not process.state == 0:
            status, msg = node.stop_process(process.group + ":" + process.name)
            if status:
                print("Process stopped!")
            else:
                print(msg)

        status, msg = node.start_process(process.group + ":" + process.name)
        if status:
            ...
            activity.logger.info(
                "{} restarted {} node's {} process.".format(
                    "不知道他娘的谁", node_name, process.name
                )
            )
        else:
            ...
            activity.logger.info(
                "{} unsuccessful restart event {} node's {} process.".format(
                    "不知道他娘的谁", node_name, process.name
                )
            )

    return resp_200()


# ------------------------------- 路由添加 --------------------------------
router.add_api_route(methods=['GET'], path="/nodes", endpoint=get_nodes,
                     summary="supervisor 获取所有 node, 仅 node 信息而不是 processes")
router.add_api_route(methods=['GET'], path="/nodes/{node_name}", endpoint=get_node, summary="supervisor 获取单个 node")
router.add_api_route(methods=['GET'], path="/nodes/{node_name}/processes", endpoint=get_node_processes,
                     summary="supervisor 获取 node processes")

router.add_api_route(methods=['GET'], path="/nodes/{node_name}/process/{unique_process_name}",
                     endpoint=get_process, summary="supervisor 获取 process")
router.add_api_route(methods=['PUT'], path="/nodes/{node_name}/process/{unique_process_name}/start",
                     endpoint=start_process, summary="supervisor 开启 process")
router.add_api_route(methods=['PUT'], path="/nodes/{node_name}/process/{unique_process_name}/stop",
                     endpoint=stop_process, summary="supervisor 停止 process")
router.add_api_route(methods=['PUT'], path="/nodes/{node_name}/process/{unique_process_name}/restart",
                     endpoint=restart_process, summary="supervisor 重启 process")
router.add_api_route(methods=['GET'], path="/nodes/{node_name}/process/{unique_process_name}/log",
                     endpoint=read_process_log, summary="supervisor process 日志")

router.add_api_route(methods=['PUT'], path="/nodes/{node_name}/all-processes/start",
                     endpoint=start_all_process, summary="supervisor 启动所有 processes")
router.add_api_route(methods=['PUT'], path="/nodes/{node_name}/all-processes/stop",
                     endpoint=stop_all_process, summary="supervisor 停止所有 processes")
router.add_api_route(methods=['PUT'], path="/nodes/{node_name}/all-processes/restart",
                     endpoint=restart_all_process, summary="supervisor 重启所有 processes")
