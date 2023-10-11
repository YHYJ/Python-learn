#!/usr/bin/env python3

"""
用到的库：
    docopt  Py3命令行参数解析
    requests    Py访问HTTP资源
    colorama    命令行着色工具
    prettytable 格式化信息打印（类似MySQL的格式）
setuptools 的使用
"""

"""用法及参数：
用法：python tickets.py [-gdtkz] <from> <to> <date>
参数：
    -h --help   显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达
例如：
    tickets 北京 上海 2016-10-10
    tickets -dg 成都 南京 2016-10-10
"""

from docopt import docopt


def cli():
    arguments = docopt(__doc__)
    print(arguments)


if __name__ == '__main__':
    cli()