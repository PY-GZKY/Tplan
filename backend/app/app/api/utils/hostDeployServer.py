# !/usr/bin/env python
# -*- coding:utf-8 -*-

from concurrent.futures import ThreadPoolExecutor

import paramiko
from app.logger import logger


class SSHConnection(object):
    def __init__(self, command):
        self.__k = None
        self.command = command

    def connect(self, host, port, username, password):
        transport = paramiko.Transport((host, port))
        transport.connect(username=username, password=password)
        return transport

    def close(self, transport):
        logger.debug(f"{transport} close ... done")
        transport.close()  # 释放资源

    def deploy(self,
               host: str = 'localhost',
               port: int = 22,
               username: str = '',
               password: str = '',
               ) -> None:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 自动设置ssh密钥对

        transport = self.connect(host, port, username, password)  # 连接远程服务器
        ssh._transport = transport  # 赋值transport

        # 执行命令
        _, stdout, stderr = ssh.exec_command(self.command, get_pty=True)

        while not stdout.channel.exit_status_ready():
            result = stdout.readline().strip('\n')
            if result:
                logger.debug(f"{host}终端输出:　{result}")
                # add_task_log(taskId=self.task_id, taskLogMsg=result, host=host)
            # 由于在退出时，stdout还是会有一次输出
            if stdout.channel.exit_status_ready():
                break

        self.close(transport)  # 关闭连接
        # return True

    def bulk_deploy(self, hosts) -> None:

        with ThreadPoolExecutor(max_workers=8) as pool:
            [
                pool.submit(self.deploy, **host_info)
                for host_info in hosts
            ]


# if __name__ == '__main__':
#     obj = SSHConnection(command="yum -y install wget")
#     obj.deploy()
