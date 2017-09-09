#--coding:utf-8--
n=int( raw_input() )
car=[]
for i in xrange(0,n):
    car.append( map(int,raw_input().split() ) )
#--------------------
#car=[ [2,2],[3,1],[5,2], [7,3]]

def oneshot(car):
    maxp=0
    for x in car:
        if x[0]+x[1]>maxp:
            maxp=x[0]+x[1]
    maxnum=0
    t=0
    for k in xrange(0,maxp):
        temp=[]
        for j in xrange(0,len(car)):
            if car[j][0]<=k and car[j][0]+car[j][1]>=k:
                temp.append(j)
        car2=[ ]
        for u in xrange(0,len(car) ):
            if u not in temp:
                car2.append(car[u])
        sec=oneshot2(car2)
        if len(temp)+len(sec)>maxnum:
            maxnum=len(temp)+len(sec)
    return maxnum

def oneshot2(car):
    maxp=0
    for x in car:
        if x[0]+x[1]>maxp:
            maxp=x[0]+x[1]
    maxnum=[]
    t=0
    for k in xrange(0,maxp):
        temp=[]
        for j in xrange(0,len(car)):
            if car[j][0]<=k and car[j][0]+car[j][1]>=k:
                temp.append(j)
        car2=[ ]
        if len(temp)>len(maxnum):
            maxnum=temp
    return maxnum



#--------------------
result=oneshot(car)

print result
