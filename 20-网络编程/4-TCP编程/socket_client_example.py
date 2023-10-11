#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: socket_client.py
Author: YJ
Email: yj1516268@outlook.com
Created Time: 2020-04-23 09:44:25

Description: 优化Socket连接的生命周期
"""

import os
import socket


class SocketClient(object):

    """Socket Client"""

    def __init__(self, config):
        self._sock = None
        self.ip = config.get('ip', '127.0.0.1')
        self.port = config.get('port', 8000)

        self.connect_timeout = config.get('timeout', {}).get('connect', 10.0)
        self.read_timeout = config.get('timeout', {}).get('read', 10.0)
        self.write_timeout = config.get('timeout', {}).get('write', 10.0)

        self._keep_alive = config.get('keep_alive', False)

    def _disconnect(self):
        """CLose socket connection
        :returns:

        """
        if self._sock is not None:
            try:
                print('Closing socket')
                self._sock.shutdown(2)  # 0 - read, 1 - write, 2 - all
                self._sock.close()
            except Exception as error:
                raise Exception(
                    ('Failed to close socket '
                     '"{address}", port {port}, error: {error}').format(
                         address=self.ip, port=self.port, error=error
                    )
                )
            self._sock = None

    def _connect(self):
        """Connect to Socket Server
        :returns:

        """
        # Create socket
        try:
            self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print(
                'Creating socket to "{address}", port {port}'.format(
                    address=self.ip, port=self.port
                )
            )
            self._sock.settimeout(self.connect_timeout)
            print(
                'Set socket connect timeout to: {0}'.format(
                    self._sock.gettimeout()
                )
            )
        except Exception as error:
            self._sock = None
            raise Exception(
                ('Failed to create socket '
                 '"{address}", port {port}, error: {error}').format(
                     address=self.ip, port=self.port, error=error
                 )
            )

        # Connect socket
        try:
            self._sock.connect((self.ip, self.port))
            print(
                'Connecting socket to "{address}", port {port}'.format(
                    address=self.ip, port=self.port
                )
            )
        except Exception as error:
            self._disconnect()
            raise Exception(
                ('Failed to connect to '
                 '"{address}", port {port}, error: {error}').format(
                     address=self.ip, port=self.port, error=error
                 )
            )

    def _send(self, request):
        """Send a data string to the socket

        :request: request
        :returns:

        """
        try:
            self._sock.sendall(request)
        except Exception as error:
            print(
                'Failed to send request error: {error}'.format(error=error)
            )
            return False

        return True

    def _receive(self):
        """Receive data from socket
        :returns: bytes

        """
        try:
            self._sock.settimeout(self.read_timeout)
            print(
                'Set socket read timeout to: {0}'.format(
                    self._sock.gettimeout()
                )
            )
            data = self._sock.recv(8192)
        except Exception as error:
            self._disconnect()
            raise Exception(
                'Failed to receive response: {error}'.format(error=error)
            )

        return data or b' '

    def query(self):
        """Get data, process data, store data

        :returns: dict

        """
        if self._sock is None:
            self._connect()
            if self._sock is None:
                return None

        # TODO: self._send(request)
        # TODO: self._receive()

        if not self._keep_alive:
            self._disconnect()

        pass

    def _write2file(self, data, filename='out.txt'):
        """Write data to file

        :data: Data to be written
        :filename: File name
        :returns:

        """
        curr_dir = os.path.dirname(os.path.abspath(__file__))

        outfile = os.path.join(curr_dir, filename)

        print(
            'Write data to "{outfile}"'.format(
                outfile=outfile
            )
        )

        with open(outfile, 'a+') as file:
            file.write('{data}{sep}'.format(data=str(data), sep='\n'))

    def run(self, to_where='console'):
        """Run
        :to_where: Destination
        :returns:

        """
        if to_where == 'console':
            # 输出到console
            pass
        else:
            # 输出到文件
            pass


if __name__ == "__main__":
    config = {
        'ip': '192.168.100.8',
        'port': 8000,
        'timeout': {
            'connect': 10.0,
            'read': 10.0,
            'write': 10.0,
        },
        'keep_alive': True,
    }
    to_where = 'socket_out.txt'

    socket_client = SocketClient(config)
    socket_client.run(to_where)
