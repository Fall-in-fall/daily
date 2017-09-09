#encoding:utf-8
n=int( raw_input() )
sam=[]
for i in xrange(0,n):
    sam.append( map( int,raw_input().split() ) )
c=raw_input()
conds=[]
for j in xrange(x,c):
    inp=raw_input().split()
    inp[2]=int(inp[2])
    conds.append(inp)

for m in conds:
    for ni in xrange(0,len(sam)):
        dox=m[1]
        val=m[2]
        condition=m[0]
        for

