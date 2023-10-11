#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student():

    def __init__(self,name):
        self.name = name

    def __str__(self):
        """定制打印的实例的内容"""
        return 'Student object (name: %s)' % self.name

    def __getattr__(self, attr):
        """调用不存在的属性时动态返回一个属性"""
        if attr == 'score':
            return 99
        # 定义了__getattr__后调用未知属性默认返回None，修改这个默认值
        raise AttributeError("\'Student\' object has no attribute \'%s\'" % attr)

    def __call__(self):
        """直接对实例进行调用"""
        print('My name is %s' % self.name)

s = Student('Mark')
print(s.name)
print(s.score)
s()             # 直接调用实例，不需要self参数
print(callable(Student))    # 类是可调用的
print(callable(s))      # 类有__call__方法时他的实例是可调用的
# print(s.a)    # 调用未知属性



class Fib():

    def __init__(self):
        self.a,self.b = 0,1     # 初始化两个计数器a,b

    def __iter__(self):
        """实现迭代"""
        return self             # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a,self.b = self.b,self.a + self.b  # 计算下一个值
        if self.a > 1000:       # 退出循环的条件
            raise StopIteration()
        return self.a           # 返回下一个值

    def __getitem__(self, n):
        """使可以按下标取出元素和简单的切片"""
        if isinstance(n,int):    # item是索引
            self.a,self.b = 1,1
            for x in range(n):
                self.a,self.b = self.b,self.a + self.b
            return self.a
        if isinstance(n,slice):  # item是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            self.a,self.b = 1,1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(self.a)
                self.a,self.b = self.b,self.a + self.b
            return L

f = Fib()
print(f[1])     # 索引
print(f[0:5])   # 切片
#for n in f:
#    print(n)



'''
__getattr__可以把一个类的所有属性和方法调用全部动态化处理而不需要任何特殊手段
这种完全动态调用的特性可以针对完全动态的情况作调用

利用完全动态的__getattr__，可以写出一个链式调用：'''
class Chain():

    def __init__(self,path='https:/'):
        self._path = path

    def __getattr__(self, path_2):
        if path_2 == 'users':
            return lambda name:Chain("%s/users/%s" % (self._path, name))
        else:
            return Chain("%s/%s" % (self._path, path_2))

    def __str__(self):
        return self._path

print(Chain().status.user.timeline.list)
print(Chain().users('YJ').repos)    # 调用时显示用户名