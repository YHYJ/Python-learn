#!/usr/bin/env python3

from redis import *

try:
    # 与redis-server建立连接
    redis_str = StrictRedis()
    result = redis_str.keys()
    if result:
        print(result)
    else:
        print(None)
except Exception as e:
    print(e)

