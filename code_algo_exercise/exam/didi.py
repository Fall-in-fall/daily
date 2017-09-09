# -*- encoding:utf-8 -*-
# def maxSubSum( arr ):
#     lastSum = arr[0]
#     cuMax = lastSum
#     for i in xrange(1,len(arr)):
#         if lastSum<0:
#             lastSum=arr[i]
#         else:
#             lastSum=arr[i]+lastSum
#         if lastSum>cuMax:
#             cuMax=lastSum
#     return cuMax
# arr = map(int,raw_input().split(' '))
# print maxSubSum(arr)

arr = map(int,raw_input().split(' '))
k = int(raw_input())
#快排实现，比较基准默认第一个元素，可修改
def didi_quicksort(all,start=0,endout=-1):
    if endout==-1:
        endout=len(all)
    if endout-start<=1:
        return
    centrePos=start #默认是第一个元素，可修改
    centreValue=all[centrePos]
    i=start
    minIndex=start
    while i<endout:
        if i!=centrePos and all[i]>centreValue:
            if i!=minIndex:
                didi_swap(all,minIndex,i)
                if centrePos==minIndex:
                    centrePos=i
            minIndex+=1
        i+=1
    didi_swap(all,minIndex,centrePos) ; centrePos=minIndex
    didi_quicksort(all,start,centrePos)
    didi_quicksort(all,centrePos+1,endout )
def didi_swap(all,x,y):
    temp=all[x]
    all[x]=all[y]
    all[y]=temp
didi_quicksort(arr)
print arr

# arr = map(int,raw_input().split(' '))
# k = int(raw_input())
# print sorted(arr,reverse=1)[k-1]