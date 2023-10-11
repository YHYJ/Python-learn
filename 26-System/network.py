#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: network.py
Author: YJ
Email: yj1516268@outlook.com
Created Time: 2019-11-19 10:10:53

Description: 获取网络相关信息
头文件：/usr/include/bits/ioctls.h
"""

import socket
import struct
from fcntl import ioctl
from psutil import net_if_addrs

DEVICE = 'wlp3s0'
IP_TABLE = 0x8915
MAC_TABLE = 0x8927

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def getIP(device):
    """获取指定设备的IP

    :device: 设备名
    :returns: device指定的设备的IP

    """
    ip_info = ioctl(
        s.fileno(), IP_TABLE, struct.pack('64s', DEVICE.encode('utf-8'))
    )
    ip = socket.inet_ntoa(ip_info[20:24])

    return ip


def getInfo(device):
    """获取指定设备的MAC

    :device: TODO
    :returns: TODO

    """
    for name, info in net_if_addrs().items():
        if name == device:
            ip = info[0][1]
            mac = info[-1][1]

    return ip, mac


ip = getIP(DEVICE)
print('{device}的信息为: [{iip}]'.format(device=DEVICE, iip=ip))

ip, mac = getInfo(DEVICE)
print('{device}的信息为: [{iip}, {imac}]'.format(device=DEVICE, iip=ip, imac=mac))
