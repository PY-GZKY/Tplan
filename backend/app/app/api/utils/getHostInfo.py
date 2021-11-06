# -*- coding:utf-8 -*-
import paramiko
from paramiko.ssh_exception import SSHException

from app.logger import logger
from app.config import settings


class HostInfo(object):
    def __init__(self):
        self.__k = None

    def connect(self, host, port, username, password):
        transport = paramiko.Transport((host, port))
        transport.connect(username=username, password=password)
        return transport

    def close(self, transport):
        logger.debug(f"{transport} close ... done")
        transport.close()  # 释放资源

    def info_(
            self,
            host: str = '',
            port: int = 22,
            username: str = '',
            password: str = '',
            command: str = None
    ) -> dict:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 自动设置ssh密钥对

        transport = self.connect(host, port, username, password)  # 连接远程服务器
        ssh._transport = transport  # 赋值transport

        # 执行命令
        _, Stdout, Stderr = ssh.exec_command(command=settings.HOST_INFO_COMMAND)
        _, PyStdout, PyStderr = ssh.exec_command(command=settings.PYTHON_VERSION_COMMAND)
        # if PyStderr:
        #     _, PyStdout, PyStderr = ssh.exec_command(command=settings.ECHO_PYTHON_VERSION_COMMAND)
        _, PipStdout, PipStderr = ssh.exec_command(command=settings.PIP_LIST_COMMAND)

        # 获取命令结果
        Stdout = Stdout.read().decode('utf8')
        Stderr = Stderr.read().decode('utf8')

        # 获取命令结果
        PyStdout = PyStdout.read().decode('utf8')
        PyStderr = PyStderr.read().decode('utf8')

        if PyStderr:
            PyStdout = "Python (版本未知)"

        # 获取命令结果
        PipStdout = PipStdout.read().decode('utf8')
        PipStderr = PipStderr.read().decode('utf8')

        # 如果错误不为空
        if Stderr:
            # raise SSHException(Stderr)
            data = {"info": Stderr, "pyInfo": PyStdout, "pipInfo": PipStdout}
        else:
            data = {"info": Stdout, "pyInfo": PyStdout, "pipInfo": PipStdout}

        # if Stdout != '':
        #     logger.debug(f'执行 {command}')
        # logger.debug(f'{host}: {Stdout}')

        self.close(transport)  # 关闭连接
        return data

# if __name__ == '__main__':
#     obj = HostInfo()
#     print(obj.info_())
