#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""datetime是Py处理日期和时间的标准库
本地时间是指系统设定时区的时间
例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间"""


from datetime import datetime, timedelta, timezone

# 获取当前日期和时间
now = datetime.now()    # 获取当前datetime
print(type(now), now)    # datetime.now()返回当前日期时间，其类型是datetime


# 获取指定日期时间
'''要指定某个日期和时间，直接用参数构造一个datetime'''
dt = datetime(2008, 8, 8, 20, 00)  # 用指定日期创建datetime
print(dt)


# datetime转换为timestamp
'''使用timestamp()方法'''
'''在计算机中，时间实际上是用数字表示的
1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time——新纪元时间,记为0（1970年以前的时间timestamp为负数）
当前时间就是相对于epoch time的秒数，称为timestamp'''
# 可以认为：
'''
timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
对应的北京时间是：
timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00
'''
# 可见timestamp的值与时区毫无关系，
'''因为timestamp一旦确定，其UTC时间就确定了
转换到任意时区的时间也是完全确定的
这就是为什么计算机存储的当前时间是以timestamp表示的
因为全球各地的计算机在任意时刻的timestamp都是完全相同的（假定时间已校准）'''
ti = datetime(1970, 1, 1, 8, 0, 0)
tt = ti.timestamp()  # 把datetime转换为timestamp
print(tt)
'''Py的timestamp是一个浮点数，如果有小数位，小数位表示毫秒数
某些编程语言（如Java和JSp）的timestamp使用整数表示毫秒数-
-这种情况下只需要把timestamp除以1000就得到Py的浮点表示方法'''

# timestamp转换为datetime
'''要把timestamp转换为datetime，使用datetime提供的fromtimestamp()方法'''
t = 11156478521.0
print(datetime.fromtimestamp(t))
'''timestamp没有时区的概念，而datetime是有时区的
上述转换是在timestamp和本地时间间转换
【本地时间】是指当前操作系统设定的时区
例如北京时区是东8区，则本地时间：
    2015-04-19 12:20:00
实际上就是UTC+8:00时区的时间：
    2015-04-19 12:20:00 UTC+8:00
而此刻的格林威治标准时间与北京时间差了8小时，也就是UTC+0:00时区的时间应该是：
    2015-04-19 04:20:00 UTC+0:00
'''
# timestamp也可以直接被转换到UTC标准时区的时间：
print(datetime.fromtimestamp(t))        # 本地时间
print(datetime.utcfromtimestamp(t))     # UTC时间


# str转换为datetime
'''很多时候，用户输入的日期和时间是字符串
要处理日期和时间，首先必须把str转换为datetime
转换方法是datetime.strptime()，需要一个日期和时间的格式化字符串'''
time = '2016-09-21 21:09:18'  # input('请输入日期和时间，格式为 xxxx-xx-xx xx:xx:xx ：')
cady = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
print(type(cady), cady)
'''转换后的datetime是没有时区信息的'''

# datetime转换为str
'''如果已经有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str
转换方法是strftime()，同样需要一个日期和时间的格式化字符串'''
now_1 = datetime.now()
nowstr = now.strftime('%Y年 %m-%d %H:%M')
print(type(nowstr), nowstr)


# datetime加减
'''对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime
加减可以直接用+和-运算符，不过需要导入timedelta这个类'''
now_2 = datetime.now()
print(now_2)
now_2 += timedelta(days=1, hours=13, seconds=2.3)   # 加1天13小时2.3秒
print(now_2)
now_2 -= timedelta(days=2)
print(now_2)


# 本地时间转换为UTC时间
'''本地时间是指系统设定时区的时间
例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间'''
'''一个datetime类型有一个时区属性tzinfo，但是默认为None
所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区：'''
tz_utc_8 = timezone(timedelta(hours=8))     # 创建时区UTC+8:00
print(tz_utc_8)
now_3 = datetime.now()
print(now_3)
dt = now.replace(tzinfo=tz_utc_8)   # 强制设置为UTC+8:00
print(dt)
'''系统时区恰好是UTC+8:00上述代码就是正确的，否则不能强制设置为UTC+8:00时区'''


# 时区转换
'''拿到UTC时间，并强制设置时区为UTC+0:00:'''
now_np = datetime.now()
now_utc = datetime.utcnow().replace(tzinfo=timezone.utc)
print('北京时间：%s  UTC时间:%s' % (now_np, now_utc))
'''astimezone()将转换时区为北京时间:'''
now_bj = now_utc.astimezone(timezone(timedelta(hours=8)))
print('UTC时间转换的北京时间：', now_bj)
'''astimezone()将转换时区为东京时间'''
now_dj = now_utc.astimezone(timezone(timedelta(hours=9)))
print('UTC时间转换的东京时间：', now_dj)
'''astimezone()将now_bj转换时区为东京时间:'''
now_dj_2 = now_bj.astimezone(timezone(timedelta(hours=9)))
print('北京时间转换的东京时间：', now_dj_2)
'''
时区转换的关键在于：拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间

利用带时区的datetime，通过astimezone()方法，可以转换到任意时区

注：不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换
例如上述now_bj到now_dj_2的转换'''


"""小结：
datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间
如果要存储datetime，最佳方法是将其转换为timestamp再存储-
-因为timestamp的值与时区完全无关
"""