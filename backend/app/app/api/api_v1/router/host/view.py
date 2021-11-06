# -*- coding: utf-8 -*
# @Time : 2020/11/10 15:00
import json
import time
import uuid

from app.api.utils.defaultKeyBuilder import default_key_builder
from app.api.utils.getHostInfo import HostInfo
from app.api.utils.hostDeployServer import SSHConnection
from app.api.utils.hostTestConnect import TestConnect
from app.api.utils.responseCode import resp_200, resp_400
from app.common.deps import get_db
from app.logger import logger
from app.models.hosts import Hosts
from app.security.security import AES_Encrypt, AES_Decrypt
from fastapi import APIRouter, Depends
from fastapi_cache import JsonCoder
from fastapi_cache.decorator import cache
from sqlalchemy.orm import Session
from starlette.requests import Request

from app import settings

router = APIRouter()


async def get_host_list(*, request: Request,
                        db: Session = Depends(get_db),
                        status: str = None,
                        ):
    total = db.query(Hosts).filter(Hosts.host_status == status).count() if status else db.query(Hosts).count()
    host_list = db.query(Hosts).filter(Hosts.host_status == status).all() if status else db.query(Hosts).all()
    items = [{
        'id': host.id,
        'host_name': host.host_name,
        'host_status': host.host_status,
        'ip': host.ip,
        'port': host.port,
        'username': host.username,
        'host_type': host.host_type,
        'is_verify': host.is_verify,
        'desc': host.desc,
        'uuid': host.uuid,
        'update_time': str(host.update_time)
    } for host in host_list]

    data = {"items": items, "total": total}
    return resp_200(data=data)


async def create(*, request: Request,
                 dict_params: dict,
                 db: Session = Depends(get_db)
                 ):
    # print(dict_params)
    # try:
    createHost = Hosts(
        host_name=dict_params.get("host_name"),
        host_type=dict_params.get("host_type", "工作节点"),
        ip=dict_params.get("ip"),
        port=dict_params.get("port"),
        username=dict_params.get("username"),
        password=AES_Encrypt(dict_params.get("password")),
        uuid=dict_params.get("uuid", str(uuid.uuid4())),
        desc=dict_params.get("desc"),
        is_verify=False,
        update_time=dict_params.get("update_time"),
    )
    db.add(createHost)
    db.commit()
    return resp_200(message='添加成功')
    # except:
    #     db.rollback()
    #     return resp_400(message='添加失败')


def update(*, request: Request,
           dict_params: dict,
           db: Session = Depends(get_db),
           ):
    hostInfo = db.query(Hosts).filter(Hosts.id == dict_params.get("id")).first()
    try:
        hostInfo.host_name = dict_params.get("host_name"),
        hostInfo.ip = dict_params.get("ip"),
        hostInfo.port = dict_params.get("port"),
        hostInfo.username = dict_params.get("username"),
        hostInfo.password = AES_Encrypt(dict_params.get("password")) if dict_params.get(
            "password") else hostInfo.password,
        hostInfo.host_type = dict_params.get("host_type", "工作节点"),
        hostInfo.host_status = dict_params.get("host_status", "未知"),
        hostInfo.desc = dict_params.get("desc"),
        hostInfo.update_time = time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime())
        db.commit()
        return resp_200(message='编辑成功')
    except:
        db.rollback()
        return resp_400(message="")


async def delete(*, request: Request,
                 dict_params: dict,
                 db: Session = Depends(get_db),
                 ):
    try:
        db.query(Hosts).filter(Hosts.uuid == dict_params.get(
            "uuid")).delete(synchronize_session=False)
        db.commit()
        return resp_200(message='删除成功')
    except:
        db.rollback()
        return resp_400(message='删除失败')


# 测试节点
async def test(*, request: Request,
               dict_params: dict,
               db: Session = Depends(get_db),
               # token_data: Union[str, Any] = Depends(deps.check_jwt_token)
               ):
    # try:
    hostInfo = db.query(Hosts).filter(
        Hosts.uuid == dict_params.get("uuid")).first()
    print(hostInfo.ip, hostInfo.username)
    testClass = TestConnect(
        host=hostInfo.ip,
        port=hostInfo.port,
        username=hostInfo.username,
        password=AES_Decrypt(hostInfo.password),
    )  # 默认端口 22

    testResult = testClass.run()
    if testResult:
        # 连接成功后更新主机状态
        hostInfo.host_status = 1
        db.commit()
    else:
        # 连接失败后更新主机状态
        hostInfo.host_status = -1
        db.commit()

    print(testResult)
    return resp_200(data=dict(ip=hostInfo.ip, hostName=hostInfo.host_name, uname=testResult),
                    message='连接成功') if testResult else resp_400(message='连接失败', data="请重新检查配置项")
    # except:
    #     db.rollback()
    #     return resp_400()


async def detail(
        *, request: Request,
        db: Session = Depends(get_db),
        uuid: str,
):
    hostInfo = db.query(Hosts).filter(Hosts.uuid == uuid).first()

    # 缓存节点详情
    @cache(namespace=hostInfo.uuid, expire=settings.HOST_CACHE_EXPIRE, coder=JsonCoder, key_builder=default_key_builder)
    async def get_host_detail(hostInfo):
        # hostInfo = db.query(Hosts).filter(Hosts.id == hostId).first()
        # 等待 redis读取
        print(f"{settings.REDIS_CACHE_KEY}{settings.HOST_DETAIL_KEY}{uuid}")
        cacheHostInfo = await request.app.state.redis.get(
            f"{settings.REDIS_CACHE_KEY}{settings.HOST_DETAIL_KEY}{uuid}")

        # 缓存失效
        if cacheHostInfo:
            print("命中缓存")
            cacheHostInfo = json.loads(cacheHostInfo)
            return cacheHostInfo
        else:
            data = {
                'id': hostInfo.id,
                'host_name': hostInfo.host_name,
                'host_status': hostInfo.host_status,
                'ip': hostInfo.ip,
                'port': hostInfo.port,
                'username': hostInfo.username,
                'host_type': hostInfo.host_type,
                'is_verify': hostInfo.is_verify,
                'desc': hostInfo.desc,
                'updateTime': str(hostInfo.update_time)
            }
            sysInfo = HostInfo().info_(host=hostInfo.ip, port=hostInfo.port, username=hostInfo.username,
                                       password=AES_Decrypt(hostInfo.password))
            logger.debug(sysInfo)
            sysInfo.update(data)
            print(sysInfo)
            # return dict(code=200, message="Success", hostInfo=sysInfo)
            return dict(code=20000, message="Success", data=sysInfo)

    return await get_host_detail(hostInfo)


def recombination_deploy_task(hosts: list, db: Session = Depends(get_db)):
    newHosts = []
    for host in hosts:
        hostDict = {}
        hostInfo = db.query(Hosts).filter(Hosts.ip == host).first()
        hostDict.update({
            'host': hostInfo.ip,
            'port': hostInfo.port,
            'username': hostInfo.username,
            'password': AES_Decrypt(hostInfo.password),  # password 解密
        })
        # print(hostDict)
        newHosts.append(hostDict)
    return newHosts


def deploys(
        *, request: Request,
        dictParam: dict,
        db: Session = Depends(get_db),
):
    # try:
    print(f"接收到的主机列表: {dictParam.get('hosts')}")
    print(f"接收到的任务ID: {dictParam.get('cmd')}")

    newHosts = recombination_deploy_task(hosts=dictParam.get('hosts'), db=db)
    SSHConnection(command=dictParam.get('cmd')).bulk_deploy(hosts=newHosts)

    # 这里显然应该添加一张节点服务的表，用于记录节点已经暗安装了那些服务并展示到页面
    # db.commit()  # 更新已部署的主机
    return resp_200(data={}, message='部署成功')


# ------------------------------- 路由添加 --------------------------------
router.add_api_route(methods=['GET'], path="s",
                     endpoint=get_host_list, summary="节点列表")
router.add_api_route(methods=['POST'], path="/create",
                     endpoint=create, summary="创建节点")
router.add_api_route(methods=['PUT'], path="/update",
                     endpoint=update, summary="编辑节点")
router.add_api_route(methods=['DELETE'], path="/delete",
                     endpoint=delete, summary="删除节点")
router.add_api_route(methods=['POST'], path="/test",
                     endpoint=test, summary="测试节点")
router.add_api_route(methods=['GET'], path="/detail",
                     endpoint=detail, summary="节点详情")

router.add_api_route(methods=['PUT'], path="/deploys",
                     endpoint=deploys, summary="部署服务(仅限于命令行)")

# router.add_api_route(methods=['PUT'], path="/uploadZip",
#                      endpoint=upload, summary="上传爬虫压缩包")
# router.add_api_route(methods=['POST'], path="/get_rsa_private_key",
#                      endpoint=get_rsa_private_key, summary="获取ssh公钥")
# router.add_api_route(methods=['POST'], path="/change_rsa_verify",
#                      endpoint=change_rsa_verify, summary="rsa免密开关")
