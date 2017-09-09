import sys

def reverseAdd(a,b):
    def reverse(x):
        maxOrder=0
        while  x /  pow(10, maxOrder)>=1:
            maxOrder+=1
        newX=0;
        for i in xrange(maxOrder-1,-1,-1):
            temp= x/pow(10, i) *pow(10, maxOrder-i-1)
            if temp+newX>sys.maxsize or temp+newX<=-sys.maxsize:
                return 0;
            newX+=temp;
            x=  x-( x/pow(10, i) ) * pow(10, i)
        return newX
    if a<1 or a>7000 or b<1 or b>7000:
        return -1
    newA=reverse(a)
    newB=reverse(b)
    return newA+newB
all=sys.stdin.readline().strip().split(',')
a=int(all[0])
b=int(all[1])
print reverseAdd(a,b)