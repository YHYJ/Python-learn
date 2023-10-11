#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""


# 一、命名空间的定义.
'''记录变量轨迹的一个字典
它的键就是变量名，值就是变量的值'''
'''在一个Py程序中任何地方，都存在几个可用的命名空间：
1、每个函数都有自己的命名空间，叫做 【局部命名空间】 ，记录了函数的变量，包括函数的参数和局部定义的变量
2、每个模块都有自己的命名空间，叫做 【全局命名空间】 ，记录了模块的变量，包括函数、类、其他导入的模块、模块级的变量和常量
3、【内置命名空间】 ，任何模块均可访问它，它存放内置函数和异常
'''


# 二、命名空间的查找顺序
'''当一行代码要使用变量 X 的值时，Py会到所有可用的命名空间查找X
按照如下顺序.
1、局部命名空间：特指当前函数或类的方法。如果函数定义了变量或者参数 X ，Py将使用它并停止搜索
2、全局命名空间：特指当前的模块。如果模块定义了变量 X ，Python将使用它并停止搜索
3、内置命名空间：对每个模块都是全局的。作为最后的尝试，Py将假设 X 是内置函数或变量
4、如果Py在这些命名空间找不到 X 将放弃查找并引发一个NameError异常，如：NameError: name 'X' is not defined。
'''
# 嵌套函数的情况：
'''
1、先在当前(嵌套或者lambda)函数的命名空间搜索
2、然后在父函数的命名空间搜索
3、接着在模块的命名空间搜索
4、最后在内置命名空间搜索
'''
'''示例'''
info = 'Adress：'
def func_father(country):
    def func_son(area):
        city = "上海"  # 此处的city变量覆盖了下面的属于父函数的city变量
        print(info + country + city + area)
    city = "北京"
    # 调用内部函数
    func_son("朝阳")

func_father("中国")
# 以上：info在全局命名空间，country在父函数的命名空间，city、area在自己函数的命名空间


# 三、命名空间的生命周期
'''不同的命名空间在不同时刻创建，有不同的生命周期
Py的特别之处在于其赋值操作总是在最里层的作用域
赋值不会复制数据——只是将命名绑定到对象
删除也是如此：“del y”只是从局部作用域的命名空间删除命名y
所有引入新命名的操作都作用于局部作用域'''
n = 1
n += 1
def func1():
    print(n)    # 可以输出
    # n = n + 1   #不可以操作
func1()
'''由于创建命名空间时，Py会检查代码并填充局部命名空间
在Py运行那行代码之前，就发现了对i的赋值，并把它添加到局部命名空间中。
当函数执行时，python解释器认为i在局部命名空间中但没有值，所以会产生错误'''
'''
1、【内置命名空间】 在Py解释器启动时创建，会一直保留不被删除
2、模块的 【全局命名空间】 在模块定义被读入时创建
   通常也会一直保存到解释器退出
3、当函数被调用时创建一个 【局部命名空间】
   当函数返回结果或抛出异常时被删除
   每一个递归调用的函数都拥有自己的命名空间
'''


# 四、命名空间的访问
# 1、局部命名空间可以 locals() 访问
'''locals返回一个记录 名字/值 的dic
这个dic的键是字符串形式的变量名字，值是变量的实际值'''
'''示例'''
def func2(i, str):
    x = 123456
    print(locals())
func2(1, "first")

# 2、全局（模块级别）命名空间可以　globals 访问
'''示例'''
gstr = "global string"

def func3(i, info):
    x = 123456789
    print(locals())
func3(1, "first")
print(globals())

# 3、locals和globalss之间的区别
'''locals是只读的，globals不是'''
def fun4(x, infor):
    a = 12345
    print(locals())
    locals()["a"] = 456
    print("a = ", a)

y = 654321
fun4(10, "second")
globals()["y"] = 98765
print("y = ", y)
'''locals实际没有返回局部命名空间，它返回的是一个拷贝
所以对他进行改变对局部命名空间中的变量值没有影响
globals返回实际的全局命名空间而不是一个拷贝
所以对globals返回的ｄｉｃ进行改动会直接影响全局变量'''


# 五、总结
'''
1、模块的命名空间不仅包括模块级的变量和常量-
-还包括所有在模块中定义的函数和类，此外还包括任何被导入到模块的东西

2、内置命名也同样包含在一个名为__builtin__模块中

3、from module import 和 import module　之间的不同：
  使用　import module，模块本身被导入，但是它保持自己的命名空间-
    -这就是需要使用模块名访问它的函数和属性：module.function的原因
  使用　from module import-
    -实际是从另一个模块将指定的函数和属性直接导入到自己的命名空间-
    -因此不需要引用它们来源的模块
'''
