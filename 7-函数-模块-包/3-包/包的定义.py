#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''包 —— 按目录来组织模块(module)形成包(Package)

'''

'''每一个包目录下面都会有一个__init__.py文件,这个文件必须存在
否则Python就把这个目录当成普通目录,而不是一个包
__init__.py可以是空文件,也可以有Python代码-
-因为__init__.py本身就是一个模块,它的模块名就是包名mycompany
'''

#导入包后，python会通过sys.path寻找包的子路径

print('*'*50,'包的使用','*'*50)
#1、import sound.effects.echo    从包中导入特定的子模块 sound.effects.echo
#   必须全名使用 —— sound.effects.echo.echofilter(input,output,delay = 0.7,atten = 4)
#   除了最后一个子项其他都是包。最后一个可以是一个模块或者包，但不允许是定义在模块中的类、函数或者变量。


#2、from sound.effects import echo   加载sound包effects子包的echo模块        ******推荐使用*******
#   使用不需要包前缀 —— echo.echofilter(input,output,delay = 0.7,atten = 4)


#3、from sound.effects.echo import echofilter    直接导入方法
#   可以直接调用函数echofilter() —— echofilter(input,output,delay = 0.7,atten = 4)