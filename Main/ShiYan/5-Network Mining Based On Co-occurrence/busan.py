#!/usr/bin/env python3

import os, sys
import jieba, math, codecs
import jieba.posseg as pseg

"""基础共现网络：
实体间的共现（关系）是一种基于统计的信息提取
关系紧密的人物往往会在文本中多段内同时出现
可以通过识别文本中已确定的实体（人名），计算不同实体共同出现的次数和比率
当比率大于某一阈值，我们认为两个实体间存在某种联系
这种联系可以具体细化，但提取过程也更加复杂
"""

"""编写 Py 代码从纯文本中提取出人物关系网络，并用 Gephi 将生成的网络可视化"""


names = {}          # 人物姓名：键为人名，值为全文出现次数
relationships = {}  # 人物关系：键为有向边的起点，值为字典edge
lineNames = []      # 当前段人物


# 识别文本中的实体
'''读入文本每一行并对其做分词（判断该词的词性是否为“人名”[词性编码：nr]，如果不为nr，则认为该词不是人名）'''
jieba.load_userdict("./files/dict.txt")     # 加载字典
with codecs.open("./files/busan.txt", "r", "utf8") as f:
    for line in f.readlines():
        poss = pseg.cut(line)       # 分词，并返回该词词性
        lineNames.append([])        # 为新读入的一段添加人物名称列表
        for w in poss:
            if w.flag != "nr" or len(w.word) < 2:
                continue    # 分词长度 <2 或词性不是“nr”则认为其不是人名
            lineNames[-1].append(w.word)    # 否则是人名，添加到列表
            if names.get(w.word) is None:
                '''names字典里没有新读入的人名，则添加人名并出现次数置为 0 '''
                names[w.word] = 0
                relationships[w.word] = {}
            names[w.word] += 1    # 该人物出现次数 +1

# 人物出现次数:
# for name, times in names.items():
#     print(name, times)

# 根据识别结果构建网络
'''对于 lineNames 中每一行中出现的所有人物两两相连
如果两个人物之间尚未有边建立，则将新建的边权值设为 1，否则将已存在的边的权值加 1
这种方法将产生很多的冗余边，这些冗余边将在最后处理'''
for line in lineNames:  # 遍历每一段
    for name1 in line:
        for name2 in line:  # 每一段的任意两人
            if name1 == name2:
                continue
            if relationships[name1].get(name2) is None:  # 两人尚未同时出现则新建项
                relationships[name1][name2] = 1
            else:
                relationships[name1][name2] = relationships[name1][name2] + 1   # 两人共同出现次数 +1


# 过滤冗余边并输出结果
'''将names和relationships输出到文本以方便 gephi 可视化处理
输出边的过程中可以过滤可能是冗余的边，假设共同出现次数少于 3 次的是冗余边，则在输出时跳过这样的边
输出的节点集合保存为 busan_node.txt ，边集合保存为 busan_edge.txt '''
with codecs.open("busan_node.txt", "w", "gbk") as f:    # 节点集合
    f.write("Id Label Weight\r\n")
    for name, times in names.items():
        f.write("{} {} {}\r\n".format(name, name, str(times)))

with codecs.open("busan_edge.txt", "w", "gbk") as f:   # 边集合
    f.write("Source Target Weight\r\n")
    for name, edges in relationships.items():
        for v, w in edges.items():
            if w > 3:
                f.write("{} {} {}\r\n".format(name, v, str(w)))