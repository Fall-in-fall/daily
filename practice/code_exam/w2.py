a=raw_input()

leftCount=0
for i in xrange(1,len(a)):
    if a[i]!=a[i-1]:
        nextSame=find(a,i,a[i])
        if nextSame==-1:
            break
        leftCount+=nextSame-i
        temp=a[i]
        a[i]=a[nextSame]
        a[nextSame]=temp


def find(a,i,x):
    if i>=len(a)-1:
        return -1
    for m in xrange(i+1,len(a)):
        if a[m]==x:
            return m
    return -1