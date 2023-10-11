#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""使用Py的smtplib发送邮件十分简单
只要掌握了各种邮件类型的构造方法，正确设置好邮件头，就可以顺利发出"""


"""构造一个邮件对象就是一个Messag对象
如果构造一个MIMEText对象，就表示一个文本邮件对象
如果构造一个MIMEImage对象，就表示一个作为附件的图片
要把多个对象组合起来，就用MIMEMultipart对象
而MIMEBase可以表示任何对象它们的继承关系如下：
Message
+- MIMEBase
   +- MIMEMultipart
   +- MIMENonMultipart
      +- MIMEMessage
      +- MIMEText
      +- MIMEImage
这种嵌套关系就可以构造出任意复杂的邮件
可以通过email.mime文档查看它们所在的包以及详细的用法
"""