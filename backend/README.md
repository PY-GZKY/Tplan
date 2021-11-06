
![Fastapi Crawl](https://img.shields.io/badge/Python-3.8-green)
![Fastapi Crawl](https://img.shields.io/badge/Celery-5.0.5-blue)
![Fastapi Crawl](https://img.shields.io/badge/Fastapi-0.4.9-red)
![Fastapi Crawl](https://img.shields.io/badge/uvicorn-0.2.2-yellow)
![Fastapi Crawl](https://img.shields.io/badge/pydantic-0.2.2-brightgreen)
![Fastapi Crawl](https://img.shields.io/badge/fabric-0.1.13-yellow)
![Fastapi Crawl](https://img.shields.io/badge/Mysql-5.7-yellow)
![Fastapi Crawl](https://img.shields.io/badge/paramiko-latest-yellow)

## 🔨 Install

```
pip install -r requirements.txt
```


## 🚀 Usage

### Arq start

```shell
arq tasks_.WorkerSettings
```

### Celery start
```shell
celery worker -A app.celery_app.worker.example -l info -Q main-queue -c 1  -P eventlet
```


## 🚀 Docker

使用容器部署是一种不错的选择。



## 📝 License

[MIT](./LICENSE)