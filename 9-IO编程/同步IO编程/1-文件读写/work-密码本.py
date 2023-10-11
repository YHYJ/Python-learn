#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件存储网站及其密码，实现增删改查功能
"""


class CodeBook:
    """密码本，增删改查"""
    # pwd = input('请输入密码：')

    def __init__(self, web='', pwd='', command=''):
        self.web = web
        self.pwd = pwd
        self.command = command
        # self.verify()

    def reminder(self):
        print("-------密码管理指令集-------")
        print("[add] ——增加", end='   ')
        print("[del] ——删除")
        print("[mod] ——修改", end='   ')
        print("[fin] ——查找")

    def verify(self):
        """确认两次密码输入是否相同"""
        pwd = input('输入新密码：')
        pwd_1 = input('再输入一次：')
        if pwd == pwd_1:
            return pwd_1
        else:
            return False

    def info(self):
        """增删改查"""
        # www = {}
        while True:
            self.command = input("请输入[]里的指令：")
            if self.command == 'add':    # 增
                text = ''
                with open("./Data/codebook.data", 'w') as fi:
                    file = fi.readlines()
                    self.web = input('请输入新增网址：')
                    for value in file:
                        text = value.split(' ')
                        if text[0] == self.web:      # 一行数据的头部和输入的网址相同
                            print('网址[%s]信息已存在' % self.web)
                            break
                        else:
                            self.pwd = input('请输入密码：')
                            fi.write(self.web + ' ')  # 记录网址，跟一个空格
                            fi.write(self.pwd + '\n')  # 记录网址的密码，换行
                            print('网址%s密码已保存，再次登录无需密码' % self.web)
                            break
                    # www[self.web] = self.pwd
            elif self.command == 'del':  # 删
                text = ''
                with open("./Data/codebook.data", 'r+') as fi:
                    file = fi.readlines()
                    print('file=', file)
                    self.web = input('请输入删除网址：')
                    yn_1 = input('确认删除[%s]密码，[1-是]或[0-否]：' % self.web)
                    if yn_1 == '1':
                        for value_1 in file:
                            text = value_1.split(' ')
                            if text[0] == self.web:      # 一行数据的头部和输入的网址相同
                                print('删除前file=', file)
                                file.remove(value_1)    # 删除该元素，就是这！！！
                                print('删除后file=', file)
                                for new in file:
                                    fi.seek(2)
                                    fi.write(new)
                                print("网址[%s]密码已删除，再次登录需要密码" % self.web)
                            else:
                                print('未保存[%s]网址信息，无法删除' % self.web)
                    else:
                        print("[info]:未进行操作")
            # elif self.command is 'mod':  # 改
            #     self.web = input('请输入更新网址：')
            #     yn_2 = input('确认修改网址%s密码，[1-是]或[0-否]：' % self.web)
            #     if yn_2 == '1':
            #         for value_2 in fi.readlines():
            #             if value_2.startswith(self.web):      # 一行数据的头部和输入的网址相同
            #                 right = self.verify()
            #                 if right:
            #                     fi.readlines()[value_2] = right
            #                     fi.flush()
            #                     # www[self.web] = pwd_1
            #                     print('网址%s密码已更新' % self.web)
            #                 else:
            #                     print('两次密码输入不一致')
            #             else:
            #                 print('未保存%s网址信息' % self.web)
            #     else:
            #         print("[info]:未进行操作")
            # elif self.command is 'fin':  # 查
            #     self.web = input('请输入查询网址：')
            #     for value_3 in fi.readlines():
            #         if value_3.startswith(self.web):  # 一行数据的头部和输入的网址相同
            #             pwd = value_3.split(' ')[1]
            #             print('%s密码是：%s' % (self.web, pwd))
            #         else:
            #             print('网址%s信息未记录' % self.web)
            elif self.command == 'q':
                break
            # if self.web in www.keys():
                #     print('%s密码是：%s' % (self.web, www[self.web]))
                # else:
                #     print('网址%s信息未记录' % self.web)



        # with open("./Data/codebook", "a") as fi:
        #     if self.command is 'add':   # 增
        #         self.web = input('请输入网址：')
        #         file = fi.write(self.web + ' ')  # 记录网址，跟一个空格
        #         self.pwd = input('请输入密码：')
        #         file = fi.write(self.pwd + '\n')        # 记录网址的密码，换行
        #     elif self.command is 'del': # 删
        #         self.web = input('请输入网址：')
        #         aff = input('确认删除该网址及其密码，请输入[是]或[否]：')
        #         if aff is '是':
        #             for value in fi.readlines():
        #                 if value is self.web:
        #                     fi.readlines().remove(value)    # 删除指定网址信息
        #             data = ''.jion(fi.readlines())
        #             file = fi.write(data)
        #         else:
        #             print("[info]:未进行操作")
        #
        #     elif self.command is 'mod': # 改
        #     elif self.command is 'fin': # 查

if __name__ == '__main__':
    code = CodeBook()
    code.reminder()
    code.info()
    # if ask == '1':
    #     code.info()
    # else:
    #     print('error')
