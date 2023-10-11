#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: YJ
Email: yj1516268@outlook.com
Created Date: 2018-12-21 01:44:04

Redis pub/sub mode.
"""

import redis


def main():
    """A simple redis pub/sub example.
    A subscriber.
    :returns: TODO

    """
    redi = redis.Redis()
    ps = redi.pubsub()
    # ps.subscribe(['<Channel>, <Channel>'])
    # ps.psubscribe(['<Channel Mode>, <Channel Mode>'])
    ps.psubscribe(['Channel?', 'Bye'])
    for im in ps.listen():
        # im = {'type': 'pmessage', 'pattern': b'<Channel Mode>', 'channel': b'<Channel>', 'data': b'<message>'}
        if im['type'] == 'message':
            print('Type <{}> channel <{}> message -- {}.'.format(
                im['type'],
                im['channel'].decode('utf-8'),
                im['data'].decode('utf-8'),
            ))
        elif im['type'] == 'pmessage':
            print('Type <{}> channel <{}/{}> message -- {}.'.format(
                im['type'],
                im['pattern'].decode('utf-8'),
                im['channel'].decode('utf-8'),
                im['data'].decode('utf-8'),
            ))


if __name__ == "__main__":
    main()
