# -*- coding: utf-8 -*
# @Time : 2020/11/11 11:09


from fastapi import FastAPI
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address


limiter = Limiter(key_func=get_remote_address)
FastAPI().state.limiter = limiter
FastAPI().add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)