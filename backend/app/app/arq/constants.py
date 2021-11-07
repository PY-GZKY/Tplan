default_queue_name = 'arq:queue'
default_worker_name = "pai"
job_key_prefix = 'arq:job:'
in_progress_key_prefix = 'arq:in-progress:'
result_key_prefix = 'arq:result:'
retry_key_prefix = 'arq:retry:'
abort_jobs_ss = 'arq:abort'
# age of items in the abort_key sorted set after which they're deleted
abort_job_max_age = 60
health_check_key_suffix = ':health-check'
# how long to keep the "in_progress" key after a cron job ends to prevent the job duplication
# this can be a long time since each cron job has an ID that is unique for the intended execution time
keep_cronjob_progress = 60

time_zone = 'Asia/Shanghai'
worker_key = "arq:worker"
task_key = "arq:task"

# 关闭 worker
worker_key_close_expire = 3600
