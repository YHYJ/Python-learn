#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: simulator.py
Author: YJ
Email: yj1516268@outlook.com
Created Time: 2020-09-25 10:53:50

Description: 模拟TCP Server主动给指定地址发送数据
"""

import sys
import time
import socket
import threading


def send_data(connect, data):
    """发送数据到client

    :connect: 和客户端之间的连接
    :data: 要发送的数据
    :returns: TODO

    """
    while connect:
        try:
            connect.send(data.encode('utf8'))
        except BrokenPipeError or ConnectionResetError:
            pass
        except KeyboardInterrupt:
            sys.exit()
        except Exception as e:
            raise e
        time.sleep(1)


if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server.bind(('0.0.0.0', 6799))
    server.listen(10)

    data = 'Simulated data'
    alert = '非法访问！'

    while True:
        sock, client = server.accept()
        if client[0] == '127.0.0.1':
            td = threading.Thread(target=send_data, args=(sock, data))
        else:
            td = threading.Thread(target=send_data, args=(sock, alert))
        td.start()
