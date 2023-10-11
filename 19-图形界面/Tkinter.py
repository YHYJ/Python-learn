#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""概念：
编写的Py代码会调用内置的Tkinter，Tkinter封装了访问Tk的接口
Tk是一个图形库，支持多个操作系统，使用Tcl语言开发
Tk会调用操作系统提供的本地GUI接口，完成最终的GUI
所以代码只需要调用Tkinter提供的接口就可以了
"""


from tkinter import *
import tkinter.messagebox as messagebox


# 第一个GUI程序
'''编写一个GUI版本的“Hello, world!”'''
'''1、导入Tkinter包'''
'''2、从Frame派生一个Application类，这是所有Widget的父容器'''
class Application(Frame):
    """从Frame派生一个Application类，这是所有Widget的父容器"""
    def __init__(self, master=None):
        """
        pack()方法把Widget加入到父容器并实现布局。pack()是最简单的布局，grid()可以实现更复杂的布局
        :param master: 
        """
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        """
        创建一个Label和一个Button，当Button被点击时，触发self.quit()使程序退出
        :return: 
        """
        self.helloLabel = Label(self, text='印下你的名字')    # 提示信息
        self.helloLabel.pack()
        self.nameInput = Entry(self)    # 文本框
        self.nameInput.pack()
        self.alertButton = Button(self, text='▽生成▽', command=self.hello)    # 确定键
        self.alertButton.pack()
        self.quitButton = Button(self, text='△结束△', command=self.quit)      # 退出键
        self.quitButton.pack()

    def hello(self):
        name = self.nameInput.get() or '博士'
        messagebox.showinfo('印记', '%s 钢印族迎接你的新生' % name)
'''在GUI中，每个Button、Label、输入框等，都是一个Widget
Frame则是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树'''
'''3、实例化Application，并启动消息循环'''
app = Application()
app.master.title('思想钢印')    # 设置窗口标题
app.mainloop()  # 主消息循环
'''GUI程序的主线程负责监听来自操作系统的消息，并依次处理每一条消息
因此，如果消息处理非常耗时，就需要在新线程中处理'''
