#encoding:utf-8

# n=int(raw_input())
# result=0
# for i in xrange(0,n):
#     s=raw_input().split()
#     result+=int(s[0])*(float(s[1])/100)
# print '%.3f'%result


# def ouchuan(s):
#     for i in xrange(0,len(s)):
#         another=s.find(s[i],i+1)
#         if another==-1:
#             continue
#         else:

#打印所有的组合情况
# def comb(all):
#     for i in xrange(0,len(all)):
#         all[i]=str(all[i])
#     result=[]
#     for i in xrange(1,len(all)+1):
#         result.extend( comb_sub(all,i) )
#     return result

#打印包含m个元素的组合情况，m个元素的组合数=第一个元素+剩下序列元素的m-个组合数
#如1234，m=2个元素的组合数等于1+[2,3,4](234的m-1组合),2+[3,4](34的m-1组合)，3+[4]
#如1234，m=3个元素的组合数等于1+[23,24,34](234的m-1组合),2+[34](34的m-1组合)

# def comb_sub(all,m):
#     result=[]
#     if m==1:
#         result=all
#     else:#每次循环将起始位置往后移1，并且保证剩下的元素数大于m-1组合数
#         for i in xrange(0,len(all)-(m-1) ):#最后至少要剩下m-1个数，如果剩下的数量都少于要组合的数量就无法组合了
#             preResult=comb_sub(all[i+1:],m-1)
#             for j in xrange(0,len(preResult)):
#                 result.append( all[i]+ preResult[j])
#     return result
# s=raw_input()
# from collections import Counter
# def isOu(ss):
#     c=Counter(ss)
#     for j in c.values():
#         if j%2!=0:
#             return False
#     return True
# def ouzichuan(s):
#     count=0
#     m=2
#     cuStart=range(0,len(s)+1-m)
#     while m<len(s):
#         newStart=[]
#         for i in cuStart:
#             if isOu( s[i:i+m] ):
#                 print s[i:i+m]
#                 count+=1
#                 newStart.append(i)
#         cuStart=newStart
#         m+=2
#     return count
# print ouzichuan(s)

# s=raw_input()
# def zichuan(s,m):
#     result=[]
#     for i in xrange(0,len(s)+1-m):
#         result.append(s[i:i+m])
#     return result
#
# from collections import Counter
# def countOu(ss):
#     count=0
#     for i in ss:
#         flag=1
#         c=Counter(i)
#         for j in c.values():
#             if j%2!=0:
#                 flag=0
#                 break
#         if flag==1:
#             count+=1
#     return count
#
# k=2
# count=0
# while k<len(s):
#     count+= countOu(zichuan(s,k) )
#     k+=2
# print count

#####360-2017实习笔试第三题
a=raw_input().split()
n=int(a[0])
m=int(a[1])
taskTime=map(int,raw_input().split())
tempR=[]
for i in xrange(0,m):
    tempR.append( int(raw_input()) )
cuTime=1
while len(tempR)!=0 and len(taskTime)!=0:
    if cuTime==taskTime[0]:
        del taskTime[0]
    else:
        t=0
        max=len(tempR)
        while t<max:
            if tempR[t] <=cuTime:
                print cuTime
                del tempR[t]
                max-=1
            else:t+=1
    cuTime+=1
if len(taskTime)==0 and len(tempR)!=0:
    for i in xrange(0,len(tempR)):
        print cuTime

