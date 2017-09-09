# -*- encoding:utf-8 -*-
#第k个斐波那契数
# k = int(raw_input())
# if k==1 or k==2:
# 	print 1
# else:
# 	last1,last2 = (1,1)
# 	now = 0
# 	for i in xrange(0,k-2):
# 		now=last1+last2
# 		last1=last2
# 		last2=now
# 	print now

#第n大的质数
# n = int(raw_input())
# primeList=[2]
# count=1
# now=2
# while count!=n:
#     now=now+1
#     isPrime = True
#     for i in primeList:
#         if now%i==0:
#             isPrime=False
#             break
#     if isPrime:
#         count+=1
#         primeList.append(now)
# print now

