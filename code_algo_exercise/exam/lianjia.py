# -*- encoding:utf-8 -*-

# 1输入n个数去重加排序
# n=int(raw_input())
# all=map(int,raw_input().split(' '))
# new =set()
# for i in all:
#     new.add(i)
# result = list(new)
# result.sort()
# print len(result)
# print ' '.join(map(str,result))

#2--------------
# all=map(int,raw_input().split(' '))
# x=int(raw_input())
# count=0
# for i in all:
#     if x+30>=i:
#         count+=1
# print count

#3-------------------
def binary_search_loop(lst,value,pos):
    low, high = 0, len(lst)-1
    currrentPos=-1
    while low <= high:
        mid = (low + high) / 2
        if lst[mid][pos] < value:
            low = mid + 1
            currrentPos=0
        elif lst[mid][pos] > value:
            high = mid - 1
            currrentPos=1
        else:
            currentPos=-1
            return mid,currentPos

    if currrentPos==0:
        return mid,currrentPos
    else:
        return mid,currrentPos

n=int(raw_input())
a = map(int,raw_input().split(' '))
qn=int(raw_input())
q = map(int,raw_input().split(' '))
hint = []
sum=1
for i in xrange(0,len(a)):
    hint.append([sum,sum+a[i]-1])
    sum+=a[i]
for x in q:
    m,posM = binary_search_loop(hint,x,0)
    #n,posN = binary_search_loop(hint,x,1)
    if posM==-1:
        print m+1
    else:
        if posM==0:
            print m+1
        else:
            print m






