# -*- encoding:utf-8 -*-

import math
maxn=32000
a=[0]*maxn
s=[0]*maxn

n = int(raw_input())
a[1]=s[1]=1;
for i in xrange(2,maxn):
    a[i]=a[i-1]+int(math.log10(float(i)))+1;#a为第i个数组的长度
    s[i]=s[i-1]+a[i];#s是前i个数组的长度

i=1;
while s[i]<n:  #确定n的位置出现在第i组
    i+=1
pos=n-s[i-1]  #pos为n在第i组的位置
le=0
i =1
while le<pos:
    le+=int(math.log10(float(i)))+1 #从第1组开始遍历第i前的每一个组，利用log10(i)+1递推第i组的长度
    i+=1
print (i-1)/int(  math.pow(10,le-pos)%10)

