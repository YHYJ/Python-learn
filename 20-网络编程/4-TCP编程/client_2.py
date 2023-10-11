#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Socket_client_2"""


import socket
import time

from threading import Thread


def doConnect(host, port):
    """TODO: Docstring for doConnect.
    :returns: TODO

    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
    except Exception:
        pass    # 关键：尝试建立连接不可行的话跳过报错再次尝试

    return sock


def main():
    """TODO: Docstring for main.
    :returns: TODO

    """
    host = '127.0.0.1'
    port = 6799

    time_tag = str(time.time())
    data = '{} - {}'.format('My Test', time_tag)

    sock = doConnect(host, port)

    for i in range(3):
        time.sleep(2)
        while True:
            try:
                sock.sendall(data.encode('utf-8'))
                sdata = sock.recv(1024).decode('utf-8')
                print('Server returned: {}'.format(sdata))
                #  time.sleep(2)
                break
            except socket.error:    # 如果报socket连接错误则尝试释放资源重新连接
                print('正在重建socket连接...')
                sock.close()
                time.sleep(2)
                sock = doConnect(host, port)
            except Exception as err:
                raise err


if __name__ == "__main__":
    #  main()
    # # or # #
    thread = Thread(target=main, name='main')
    thread.setDaemon(True)
    thread.start()
    thread.join()
