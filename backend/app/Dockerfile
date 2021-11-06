FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN echo \
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster main contrib non-free\
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-updates main contrib non-free\
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-backports main contrib non-free\
deb https://mirrors.tuna.tsinghua.edu.cn/debian-security buster/updates main contrib non-free\
    > /etc/apk/sources.list

RUN apk update

RUN mkdir /code
WORKDIR /code
RUN pip install pip -U -i https://pypi.tuna.tsinghua.edu.cn/simple
ADD requirements.txt /code/
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
ADD .. /code/


# COPY ./entrypoint.sh .

# run entrypoint.sh 在 shell 脚本执行数据库迁移 并生效
# ENTRYPOINT ["./entrypoint.sh"]