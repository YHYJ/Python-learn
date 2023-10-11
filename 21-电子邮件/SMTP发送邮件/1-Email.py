#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Email的历史比Web还要久远，目前Email也是互联网上应用非常广泛的服务
几乎所有的编程语言都支持发送和接收电子邮件
"""


# MUA：Mail User Agent ——邮件用户代理
'''
假设发件人是me@163.com，收件人是friend@sina.com（虚构）
用电子邮件软件写好邮件，填上对方的Email地址，点“发送”电子邮件就发出去了
电子邮件软件被称为MUA：Mail User Agent ——邮件用户代理
'''

# MTA：Mail Transfer Agent ——邮件传输代理
'''
Email从MUA发出去，不是直接到达对方电脑
而是发到MTA：Mail Transfer Agent ——邮件传输代理
就是那些Email服务提供商，比如网易、新浪等
由于是163.com，所以Email首先被投递到网易提供的MTA
再由网易的MTA发到对方服务商，也就是新浪的MTA
这个过程中间可能还会经过别的MTA
'''

# MDA：Mail Delivery Agent ——邮件投递代理
'''
Email到达新浪的MTA后，由于对方使用的是@sina.com的邮箱
新浪MTA把Email投递到最终目的地MDA：Mail Delivery Agent ——邮件投递代理
Email到达MDA后就放在新浪的某个服务器上，存放在某个文件或特殊的数据库里
这个长期保存邮件的地方称之为电子邮箱
'''

'''
Email不会直接到达对方的电脑，因为对方电脑不一定开机，开机也不一定联网
对方要取到邮件，必须通过MUA从MDA上把邮件取到自己的电脑上
'''

#　一封电子邮件的旅程：
'''
发件人 -> MUA -> MTA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人
'''

# 编写程序发送和接收邮件，本质上是：
'''
编写MUA把邮件发到MTA
编写MUA从MDA上收邮件
'''

# SMTP：Simple Mail Transfer Protocol
'''
发邮件时，MUA和MTA使用的协议是SMTP：Simple Mail Transfer Protocol
后面的MTA到另一个MTA也是用SMTP协议
'''

# POP：Post Office Protocol，目前版本是3，俗称POP3
# IMAP：Internet Message Access Protocol
'''
收邮件时，MUA和MDA使用的协议有两种 ——
    POP：Post Office Protocol，目前版本是3，俗称POP3
    IMAP：Internet Message Access Protocol，目前版本是4-
        -优点是不但能取邮件，还可以直接操作MDA上存储的邮件
        -比如从收件箱移到垃圾箱等
'''

'''
邮件客户端软件在发邮件时，会提示先配置SMTP服务器，也就是要发到哪个MTA上
假设正在使用163的邮箱，就不能直接发到新浪的MTA上，因为它只服务新浪的用户
所以得填163提供的SMTP服务器地址：smtp.163.com
为了证明是163的用户，SMTP服务器还要求填写邮箱地址和邮箱口令
这样，MUA才能正常地把Email通过SMTP协议发送到MTA

类似的，从MDA收邮件时，MDA服务器也要求验证邮箱口令，确保不会有其他人收取邮件
所以，Outlook之类的邮件客户端会要求填写POP3或IMAP服务器地址、邮箱地址和口令
这样，MUA才能顺利地通过POP或IMAP协议从MDA取到邮件
'''

'''
在使用Py收发邮件前，先准备好至少两个邮箱，注意两个邮箱不要用同一家邮件服务商
最后特别注意，目前大多数邮件服务商都需要手动打开SMTP发信和POP收信的功能
否则只允许在网页登录
'''
