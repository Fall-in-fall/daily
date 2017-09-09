# -*- encoding:utf-8 -*-
# all = map(int,raw_input().split(' '))
# 给定序列1,22,333，给出一个数m，求m是序列中的第几项
# import math
# m = int(raw_input())
#
# def allen(n):
#     return 0.5*n*(1+n)
#
# end = int(math.sqrt(2*m))
# while end>0:
#     if allen(end)<m:
#         break
#     end-=1
# print end+1

#-------------------------2题

# import math
# n = int(raw_input())
# allCount = 0
# for a in xrange(1,n+1):
#     for b in xrange(1, n + 1):
#         for c in xrange(1, n + 1):
#             for d in xrange(1, n + 1):
#                 if (math.pow(a, b) == math.pow(c, d)):
#                     allCount+=1
# print allCount

import math
for n in xrange(1,100):
    allCount = 0
    for a in xrange(1,n+1):
        for b in xrange(1, n + 1):
            for c in xrange(1, n + 1):
                for d in xrange(1, n + 1):
                    if (math.pow(a, b) == math.pow(c, d)):
                        allCount+=1
    print allCount

#----------------
# import math
# n = int(raw_input())
# allCount = n*n
# def getFactors(number):
#     sqrt_n = int(math.sqrt(n))
#     result = []
#     for i in xrange(2,sqrt_n+1):
#         thepow = math.pow(number, 1.0/i)
#         if int(thepow) == thepow:
#             result.append([thepow,i])
#     return result
# for i in xrange(2,n+1):
#     allCount+= n
#     allCount += len( getFactors(i))*i
# print allCount