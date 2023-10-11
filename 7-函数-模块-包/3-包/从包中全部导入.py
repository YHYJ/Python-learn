#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import test.one.test1   #从包中导入特定的子模块 test.one.test1
test.one.test1.shuchu(0)    #必须全名使用


from test.one import test1  #加载sound包effects子包的echo模块       ******推荐使用*******
test1.shuchu(1)     #使用不需要包前缀


from test.one.test1 import shuchu
shuchu(2)



#在导入一个包时，也导入了它的__init__.py文件，可以在也__init__.py中再导入其他包或者模块：
'''例如：

# 文件 __init__.py
import sys
import users
……
'''
#这样，当我们导入这个包时，__init__.py自动运行帮我们导入其中指定的模块，可减少代码量



"""从包中全部导入 *.（一般不推荐使用）

以 from test.one import * 方式进行’全部导入‘
"""
#这时import会把 __init.py__ 中定义的名为 __all__ 的列表中的子包和子模块导入到当前域：
'''例如：

# 文件 __iniy__.py
__all__ = ['module1','module2','module3']
'''
#如果 __all__ 没有定义，
# from test.one import * 不会从包test.one导入所有子包，它仅确保test.one已经导入，但：
'''
import test.one.test1
from test.one import *
'''
#这样，from …… import …… 语句之前的import导入的，模块会导入到当前域