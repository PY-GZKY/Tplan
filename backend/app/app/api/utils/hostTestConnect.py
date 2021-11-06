# # -*- coding: utf-8 -*
# # @Time : 2021/1/9 9:21

import paramiko
from paramiko.ssh_exception import SSHException

from app.logger import logger



class TestConnect():
    def __init__(self, host, port, username, password, command='uname -o -n'):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.command = command

    def connect(self, host, port, username, password):
        # print(host, port)
        transport = paramiko.Transport((host, port))
        transport.connect(username=username, password=password)
        return transport

    def close(self, transport):
        logger.debug(f"{transport} close ... done")
        transport.close()  # 释放资源

    def getUname(self) -> str:
        # print(self.command)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 自动设置ssh密钥对

        transport = self.connect(self.host, self.port, self.username, self.password)  # 连接远程服务器
        ssh._transport = transport  # 赋值transport

        # 执行命令, 监听命令每行结果
        stdin, stdout, stderr = ssh.exec_command(self.command,get_pty=True)

        # 获取命令结果
        # stdout_str = stdout.read().decode('utf8')
        # stderr_str = stderr.read().decode('utf8')

        result_ = ""
        while not stdout.channel.exit_status_ready():
            result = stdout.readline().strip('\n')
            if result:
                result_ = result
                print(f"监听输出命令行:　{result_}")

            # 由于在退出时，stdout还是会有一次输出，因此需要单独处理，处理完之后，就可以跳出了
            if stdout.channel.exit_status_ready():
                break

        # 如果错误不为空
        # if stderr_str: raise SSHException('ssh 执行错误')
        # if stdout_str != '':
        #     logger.debug(f'执行 {self.command}')
            # logger.debug(f'{stdout_str}')

        self.close(transport)  # 关闭连接
        return result_

    def run(self):
        try:
            return self.getUname()
        except SSHException:
            return None


if __name__ == '__main__':
    h = TestConnect(host='', port=22, username='', password='')
    testResult = h.run()
    print("测试结果： ", testResult)
