#encoding:utf-8
# n=int( raw_input() )
# all=[]
# for i in xrange(0,n):
#     all.append( map(int,raw_input().split()) )
#
# count=0
# cuTime=0
# for o in all:
#     if cuTime+o[0]>=o[1]:
#         count+=1
#     else:
#         cuTime+=o[0]
# print count

n=int( raw_input() )
all=[]
for i in xrange(0,n):
    all.append( map(int,raw_input().split()) )
count=0
sortAll=sorted(all,key=lambda s:s[0],reverse=True)

cuLimit=0
cuTime=0
removeList=[]
for k in xrange(0,len(all) ):
    cuLimit=all[k][1]-cuTime-all[k][0]
    if cuLimit<0:
        count+=1
        removeList.append(k)
        continue
    for i in xrange(0,len(sortAll) ):
        if i not in removeList:
            if sortAll[i][0]+all[k][0]<cuLimit:
                cuLimit-= sortAll[i][0]
                removeList.append(i)
            if cuLimit==0:
                break
    cuTime+=cuLimit
print count
# 时间限制：C/C++语言 1000MS；其他语言 3000MS
# 内存限制：C/C++语言 65536KB；其他语言 589824KB
# 题目描述：
# 小明开了家饮食店。每到用餐点，都会收到一批的外卖订单（为了方便，假设订单同时到达）。每个用户都不希望等太久，所以当他们在预期的时间内外卖还没送到时，就会给小明的店评上差评。小明想知道如何去完成这些订单，才能使得获得的差评最少。
# 输入
# 第一行是一个整数N，表示有N个订单。
#
# 接下来N行每行两个整数T1、T2，表示完成这份订单并送到用户手中需要T1的时间，且必须在时间区间[0,T2]这段时间内完成，否则用户就会很生气地给一个差评。
#
# 数据范围：N<=100000，对于每一个订单0<T1<=T2< 2^31
#
# 输出
# 小明收到的差评最少是多少。
#
# 样例输入
# 4
# 100 300
# 200 1300
# 1000 1250
# 2000 3200
# 样例输出
# 1
#
# Hint
# [0,100]时间内完成订单1，因为100<=300故可以收到好评；