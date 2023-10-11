#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##########1、将文件读写加入到猜数字游戏——增加保存成绩功能
##########2、为玩家建立账户，分别保存其游戏数据

"""
lines——存放文件里按行分割后的数据成字符串，此时数据按行分割但每组数据都存放在lines中
scores——字典
s——将lines中的字符串按空格分割，每组数据分别存放在一个s中
score——查找当前玩家名字并赋给score，以便判断是否有当前玩家
"""
from random import randint

name = input('请输入你的名字：')    #输入玩家名字

f = open('./data/game.data')            #打开game.txt
lines = f.readlines()       #将文件里的数据按行分割存入到lines中
#print('lines=',lines)
f.close()

scores = {}     #初始化一个空字典
for i in lines:
    s = i.split()       #将每一行的数据拆分成list存放在s
    #print('s=',s)
    scores[s[0]] = s[1:]    #第一项作为key，后面的作为value
score = scores.get(name)    #查找当前玩家的数据。字典类的get方法是按照给定key寻找对应项，如果不存在这样的key，就返回空值None
if score is None:   #如果没找到
    score = [0,0,0]     #初始化数据

#将数据读进来后，分别存入到三个变量中
game_times = int(score[0])      # game_times 存放总游戏次数
min_times = int(score[1])       # min_times 存放最快猜出来的轮数
total_times = int(score[2])     # total_times 猜过的总轮数
'''添加变量 avg_times —— 用于存放平均轮数，
通过【猜过的总轮数】与【总游戏次数】相除得到，
因为0不能作为除数，所以加上判断条件'''
if game_times > 0:
    avg_times = float(total_times) / game_times
else:
    avg_times = 0

#在玩家开始猜之前，输出之前的成绩信息：
print('#-#-# 玩家%s：已进行%d次游戏，最快记录为%d次猜出答案，平均%.2f次猜出答案 #-#-#'%(name,game_times,min_times,avg_times))

num = randint(1,100)
times = 0       #记录每次游戏所用的轮数
guess = False
print('猜一个数字，范围是0~100！')

while guess == False:
    times += 1      #轮数+1
    answer = int(input('请输入你猜的数字：'))

    if answer < num:
        print('%d 太小！'%answer)
        #print(answer)

    elif answer > num:      #elif等效于C的else if，后面加条件
        print('%d 太大！'%answer)
        #print(answer)

    else:                  #else后面不能加条件
        print('恭喜猜对！！！')
        print('这个数字是 %d'%answer)
        guess = True
    if answer < 0 or answer > 100:
        print('注意范围为0~100，即将退出游戏！')
        break

#如果是第一次玩，或者轮数比最小轮数少，则更新最小轮数 min_times
if game_times == 0 or times < min_times:
    min_times = times
total_times += times    #总轮数增加
game_times +=1          #总游戏次数增加

#把成绩更新到对应的玩家数据中
#加str转成字符串，为后面的格式化做准备
scores[name] = [str(game_times),str(min_times),str(total_times)]
result = ''     #初始化一个空字符串，用来存放数据
for n in scores:
    #把成绩按照“name game_times min_times total_times”格式化
    #结尾加上\n换行
    line = n + ' ' + ' '.join(scores[n]) + '\n'
    result += line  #添加到result中
    #print(result)

f = open('./data/game.data','w')
f.write(result)
f.close()

#eval(input('回车键退出'))