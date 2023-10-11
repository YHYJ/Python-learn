#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
n个函数——>模块,n个模块——>包
"""

"""一个abc.py文件就是一个abc模块，一个xyz.py文件就是一个xyz模块
假设abc和xyz这两个模块名字与其他模块冲突了,可以通过包来组织模块,避免冲突
方法是选择一个顶层包名,比如mycompany
"""
# 按照如下目录存放：
'''
mycompany/
    __init__.py
    abc.py
    xyz.py
'''
'''引入了包以后,只要顶层包名不与别人冲突,那所有模块都不会冲突
现在,abc.py的模块名变成了mycompany.abc
同样,xyz.py的模块名变成了mycompany.xyz
'''
'''每一个包目录下面都会有一个__init__.py文件,这个文件必须存在
否则Python就把这个目录当成普通目录,而不是一个包
__init__.py可以是空文件,也可以有Python代码-
-因为__init__.py本身就是一个模块,它的模块名就是包名mycompany
'''


"""可以有多级目录，组成多级层次的包结构"""
# 目录结构如下：
'''
mycompany/
    webfunc/
        __init__.py
        utils.py
        www.py
    __init__.py
    abc.py
    utils.py
    xyz.py
'''
'''文件www.py的模块名是mycompany.webfunc.www
两个utils.py的模块名分别是mycompany.utils和mycompany.webfunc.utils
'''