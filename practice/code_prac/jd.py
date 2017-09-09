#--coding:utf-8--
import sys
import math
# result=[]
# while True:
#     n=raw_input()
#     if n=='':
#         break
#     all=map(int,n.split())
#     t=all[0]
#     tp=all[0]
#     for x in xrange(0,all[1]-1):
#         tp=math.sqrt(tp)
#         t+=tp
#     result.append(t)
# for i in result:
#     print '%.2f'%i


# import sys
# import math
# while True:
#     n=raw_input()
#     if n=='':
#         break
#     all=map(int,n.split())
#     t=all[0]
#     tp=all[0]
#     for x in xrange(0,all[1]-1):
#         tp=math.sqrt(tp)
#         t+=tp
#     print '%.2f'%t

# 2题
# 时间限制：C/C++语言 1000MS；其他语言 3000MS
# 内存限制：C/C++语言 65536KB；其他语言 589824KB
# 题目描述：
# 收到情报，有批新造的机器人要运输到前线。小C将去破坏机器人的运输。小C将激光炮放置在公路的一旁，等运输车经过的时候发射（假设激光炮一定可以射穿车辆）。由于能源有限，激光炮只能发射两次。可以认为激光炮放在坐标轴的原点处，并向y轴正方向发射。每辆运输车可以看作是一个矩形，起始的x轴坐标为Xi ,所有的车均位于第一象限，长度为Li,速度为1，朝x轴负方向运动。即经过t时间后，该车车头的x坐标为Xi-t，车尾坐标为Xi-t+Li 。只要打中车的任何一个部分就算击中。
# 请你算算，他在哪两个时刻发射，才能摧毁最多的运输车。
#
# 输入
# 第一行一个正整数 n ( 2≤N≤200 )，表示运输个的数量。
# 接下来n行，每行两个整数X和L(1≤X、L≤109)，表示一辆车的x轴坐标和长度。
# 输出
# 输出最多可以摧毁的运输车数量。
#
# 样例输入
# 4
# 2 2
# 3 1
# 5 2
# 样例输出
# 4
#
# Hint
# 第一炮在第3秒发射，击中1号和2号运输车，此时1号和2号车身的x坐标范围分别为[-1,1]和[0,1]；
# 第二炮在第7秒发射，击中3号和4号运输车，此时3号和4号车身的x坐标范围分别为[-2,0]和[0,3]；