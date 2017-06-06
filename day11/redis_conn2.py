# -*- coding:utf-8 -*-
__author__ = 'liulin'

import redis,time

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)

r = redis.Redis(connection_pool=pool)

# pipe = r.pipeline(transaction=False)
pipe = r.pipeline(transaction=True)

pipe.set('name', 'alex')
time.sleep(5)
pipe.set('role', 'sb')

pipe.execute()