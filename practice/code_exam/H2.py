#encoding:utf-8

#给一个筛子和指令，通过指令输出执行某种翻转筛子后的观察情况
def change(sz,m):
    r=sz[:]
    if m=='L':# 左0 右1 前2 后3 上4 下5
        r[5]=sz[0]
        r[0]=sz[4]
        r[4]=sz[1]
        r[1]=sz[5]
    elif m=='R':
        r[5]=sz[1]
        r[1]=sz[4]
        r[4]=sz[0]
        r[0]=sz[5]
    elif m=='F':
        r[5]=sz[2]
        r[2]=sz[4]
        r[4]=sz[3]
        r[3]=sz[5]
    elif m=='B':
        r[5]=sz[3]
        r[3]=sz[4]
        r[4]=sz[2]
        r[2]=sz[5]
    elif m=='A':# 左0 右1 前2 后3 上4 下5
        r[2]=sz[0]
        r[1]=sz[2]
        r[3]=sz[1]
        r[0]=sz[3]
    elif m=='C':# 左0 右1 前2 后3 上4 下5
        r[2]=sz[1]
        r[1]=sz[3]
        r[3]=sz[0]
        r[0]=sz[2]
    return r
import sys
all=sys.stdin.readline().strip()
p=[1,2,3,4,5,6]
for i in all:
    p=change(p,i)
final=''
for x in p:
    final+=str(x)
print final