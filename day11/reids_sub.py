# -*- coding:utf-8 -*-
__author__ = 'liulin'

from redis_helper import RedisHelper

obj = RedisHelper()
redis_sub = obj.subscribe()

while True:
    msg= redis_sub.parse_response()
    print(msg)
#发布者：