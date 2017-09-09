#encoding:utf-8
a=int(raw_input())
o=raw_input()
all=o.split(':')
result=''
adds=[]

if a==0:
    s=-1
    for i in xrange(0,len(all)):
        for y in xrange(0,6):
            if all[i][y]!='0':
                s=y
                break
        if s!=-1:
            adds.append(all[i][s:])
            s=-1
        else:
            adds.append('')
    result=':'.join(adds)

elif a==1:
    x=0
    for i in xrange(0,len(all)):
        if len(all[i])==0:
            adds.append('0'*6)
        elif len(all[i])!=6:
            adds.append( ('0'*(6-len(all[i])) +all[i]) )
        else:
            adds.append(all[i])
    result=':'.join(adds)
print result
