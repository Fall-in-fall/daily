# -*- encoding:utf-8 -*-

#!/bin/python
import sys
import os
import math

# /*请完成下面这个函数，实现题目要求的功能*/
# /*当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^ */
#/******************************开始写代码******************************/
# 马路信号灯，信号灯会间隔固定的时间改变状态(可通过/不可通过)。求从一点到另一点的最短时间

# 我也是这道题，感觉简单点想，就是个最短路径。
# 我看了下题目，是不是这个意思？
#
# 输入第一行是路口的个数n，下面有n行是说对应的路口的允许通过情况；
# 比如输入：
# 2
# 0，2
# 1，3
# 意思是，两个路口；
# 然后第0个路口，0-2时刻允许通过，2-4不允许，4-6允许，6-8不允许。
# 第1个路口，0-3允许，3-6不允许，6-9允许。
#
# 然后下面输入是路的条数，用来连接路口的，对应的每个路有通过所需的时间。
# 比如输入：
# 2
# 0，2，3
# 2，3，4
# 意思是，有两条路，第一条路从路口0到路口2，需要走3个时间单位；第二条路从路口2到路口3，需要走4个时间单位。
#
# 再下面输入，是起点和终点路口，比如3，5
#
# 要求输出：0时刻出发的话，输出最短时间。
#
# 我老是感觉我理解的有问题，你们是怎么理解的？
#
# 按照我的理解方式，感觉并不需要visit[]标记是否已经经过过这个路口，觉得因为有可能在路口需要等，假如绕了一小圈后回到原来经过的路口，但是由于currenttime时间点特别好，后面需要等的时间基本没有，那么比以前节省的时间是否会多余绕一圈花的时间？
#
# 还有，到达一个路口之后，经过这个路口有可能需要等，用currenttime/路口变化间隔，判断商是奇数还是偶数，偶数直接通过，奇数的话，需要等 路口变化间隔-（currenttime%路口变化间隔）的时间。然后用currenttime加上这个等的时间，然后再进入下面的递归。
#
# 递归过程中，每次跟新start地点，一旦start==end，判断mintime是否大于，currenttime，大于的话，更新mintime；
# 每次递归的话，判断currenttime是否已经大于已有的mintime，如果大于，直接返回，结束这条路径的递归。
#
# 我想知道上面的思路对不对




def minTravelTime(N,intersections,M,roads,s,t):
#/******************************结束写代码******************************/

    _N = int(raw_input())

    _intersections = []
    for i in range(0,_N):
        x,y = raw_input().split(',')
        _intersection= [int(x),int(y)]
        _intersections.append(_intersection)

    _M = int(raw_input())
    _roads= []
    for j in range(0,_M):
        u,v,w = raw_input().split(',')
        _road= [int(u),int(v),int(w)]
        _roads.append(_road)

    _s,_t = raw_input().split(',')
    _s,_t = int(_s),int(_t)

    minTime = minTravelTime(_N,_intersections,_M,_roads,_s,_t)

    print str(minTime)+"\n"