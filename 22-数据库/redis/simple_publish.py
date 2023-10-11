#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: YJ
Email: yj1516268@outlook.com
Created Date: 2018-12-21 01:33:20

Redis pub/sub mode.
"""

import time

import redis


def main():
    """A simple redis pub/sub example.
    A publisher.
    :returns: TODO

    """
    redi = redis.Redis()
    while redi.ping():
        # rediis.Redis.publish(channel, message)
        redi.publish('Channel1', '1 Test')
        time.sleep(1)
        redi.publish('Channel2', '2 Test')
        time.sleep(1)
        redi.publish('Bye', 'exit')
        time.sleep(1)


if __name__ == "__main__":
    main()
