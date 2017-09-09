#--coding:utf-8--
import sys
def H1():
    a=raw_input()
    b=raw_input()
    count=0
    for i in a:
        if i==b:
            count+=1
    print count
def h2():#每组输入n个数，多组是连续的所以需要一直读：去重并排序输出
    import sys
    while True:
        try:
            n=int(sys.stdin.readline())
        except:break
        all=[]
        t=0
        for i in xrange(0,n):
            t=int( raw_input() )
            if t in all: continue
            else: all.append(t)
        h2_quicksort(all)
        for x in xrange(0,len(all)):
            print all[x]
#快排实现，比较基准默认第一个元素，可修改
def h2_quicksort(all,start=0,endout=-1):
    if endout==-1:
        endout=len(all)
    if endout-start<=1:
        return
    centrePos=start #默认是第一个元素，可修改
    centreValue=all[centrePos]
    i=start
    minIndex=start
    while i<endout:
        if i!=centrePos and all[i]<centreValue:
            if i!=minIndex:
                h2_swap(all,minIndex,i)
                if centrePos==minIndex:
                    centrePos=i
            minIndex+=1
        i+=1
    h2_swap(all,minIndex,centrePos) ; centrePos=minIndex
    h2_quicksort(all,start,centrePos)
    h2_quicksort(all,centrePos+1,endout )

def h2_swap(all,x,y):
    temp=all[x]
    all[x]=all[y]
    all[y]=temp

def h3_yanghui(n,i):
    if i<1 or i>1+2*(n-1):
        return 0
    elif n==1:
        return 1
    else: return h3_yanghui(n-1,i-2)+h3_yanghui(n-1,i-1)+h3_yanghui(n-1,i)

n=83
for i in xrange(2,2*(n-1)):
    a=h3_yanghui(n,i)
    if a%2==0:
        print i
        break

