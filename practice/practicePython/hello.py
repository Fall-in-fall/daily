#!/usr/bin/python
# -*- coding: UTF-8 -*-

#matlab文件名

# kernel = np.exp(-kernel_shape/np.mean(kernel_shape)) + np.exp(-kernel_colour/np.mean(kernel_colour)) \
#          + np.exp(-kernel_texture/np.mean(kernel_texture)) + np.exp(-kernel_hog/np.mean(kernel_hog)) \
#          + np.exp(-kernel_hsv/np.mean(kernel_hsv)) + np.exp(-kernel_siftint/np.mean(kernel_siftint)) \
#          + np.exp(-kernel_siftbdy/np.mean(kernel_siftbdy))

import matplotlib.pyplot as plt

class xx:
    def a(self,k):
        print 'a',k
        ak=k
        ak[0]=111
        print 'k',k
        return 1,2

    def b(self):
        print 'b'

# funcs={0:xx.a,1:xx.b}
# t=xx()
# ar=1
# (p,q)=t.a([1])
# print ar
# def addTime4Predict(data, num, way=1):
#     itemIds=data[0] ; allItemData=data[1]
#     if way==1:
#         for m in xrange(len(allItemData)):
#             stores=allItemData[m]
#             for n in xrange(len(stores)):
#                 storeData=stores[n]
#                 for o in xrange(num):
#                     lastDate=storeData[-1][0]
#                     storeData.append([lastDate+1,0])
#     return [itemIds,allItemData]
#
# q=[[0,1],[[[[0,1],[1,2],[2,3],[3,4]],[[0,1.1],[1,2.2],[2,3.3],[3,4.4]]],[[[0,1],[1,2],[2,3],[3,4]],[[0,1.1],[1,2.2],[2,3.3],[3,4.4]]]]]
# print addTime4Predict(q,2)

def aa():
    try:
        raise  Exception('xx')
        print 0
    except:
        print 1

aa()
q=raw_input('xx\n')
print q