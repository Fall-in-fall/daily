# import sys
# a=sys.stdin.readline().strip()
# b=sys.stdin.readline().strip()
# k=a.split()[1]
# n=map(int,b.split())

n=[1,2,3];k=2

def change(n):
    begin=n[0]
    for i in xrange(len(n)):
        print 'before: ',n[i]
        if i==len(n)-1:addOne=begin
        else : addOne=n[i+1]
        n[i]=n[i]+addOne
        if n[i]>100:
            n[i]=n[i]%100
        print 'after: ',n[i]
while k>0:
    change(n)
    k=k-1
result=''
for x in n:
    result+=' '+str(x)
print result[1:]
#########
kk=k
for i in n:
    j=i+1
    while kk>0 and j<len(n)-1:
        n[i]=n[i]+kk*n[j]
        j=j+1
        kk=kk-1



