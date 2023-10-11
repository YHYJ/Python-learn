#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student():
    pass


"""在绑定属性时，如果直接把属性暴露出去，虽然写起来很简单但是，没办法检查参数"""
# 导致可以把成绩随便改：
s = Student()
s.score = 9999


'''成绩9999显然不合逻辑
为了限制score的范围，可以通过一个set_score()方法来设置成绩-
-再通过一个get_score()来获取成绩'''
# 这样，在set_score()方法里，就可以检查参数：
# class Student(object):

#     def get_score(self):
#         return self._score

#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
# 现在，对任意的Students实例进行操作，就不能随心所欲地设置score了：
'''ss = Students()
ss.set_score(60)        # 可以设置为60
print(ss.get_score())
ss.set_score(160)        # 不可以设置为160
print(ss.get_score())'''


class Students():

    @property   # Py内置的@property装饰器负责把一个方法变成属性调用
    def score(self):
        """把一个getter变成属性"""
        return self._score

    """@property本身又创建了一个装饰器@score.setter"""

    @score.setter
    def score(self, value):
        """负责把一个setter方法变成属性来赋值"""
        if not isinstance(value, int):
            raise ValueError('分数必须是整数！')
        if value < 0 or value > 100:
            raise ValueError('分数在0~100之间！')
        self._score = value


ss = Students()
ss.score = 100
print(ss.score)


print("*"*25, "work", "*"*25)


class Screen():
    """利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution"""

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value_w):
        self._width = value_w

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value_h):
        self._height = value_h

    @property
    def resolution(self):
        return self._width * self._height


sc = Screen()
sc.width = 1024
sc.height = 768
print(sc.resolution)
assert sc.resolution == 786432, '1024 * 768 = %d ?' % sc.resolution
