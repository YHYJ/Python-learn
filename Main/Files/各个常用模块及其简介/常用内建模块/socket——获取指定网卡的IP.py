#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: socket——获取指定网卡的IP.py
Author: YJ
Email: yj1516268@outlook.com
Created Time: 2020-12-04 17:10:00

Description: 仅适用于Linux，因为Windows没有fcntl模块
"""

import fcntl
import socket
import struct


def get_address(iface: str):
    """获取指定网络接口的IP地址

    :iface: 网络接口名
    :returns: 指定网络接口的IP，类型为'str'

    宏'SIOCGIFADDR'在/usr/include/linux/sockios.h中定义
    宏'IFNAMSIZ'在/usr/include/net/if.h中定义

    """
    SIOCGIFADDR = 0x8915  # get PA address
    IFNAMSIZ = 16  # Length of interface name

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建socket对象
    fd = sock.fileno()  # 获取socket的文件描述符

    iface_bytes = iface.encode('UTF-8')
    ifreq = struct.pack('256s', iface_bytes[:IFNAMSIZ - 1])
    ip = socket.inet_ntoa(fcntl.ioctl(fd, SIOCGIFADDR, ifreq)[20:24])

    return ip
