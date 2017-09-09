#encoding:utf-8


#打印排列组合-递归：
#每次取序列中的一个元素作为头，每个头引导包含的排列情况数  等于剩下其余元素的所有排列情况
#因此递归执行这个过程，当前序列只剩一个元素时，则排列就是它自己
def perm_sub(all):
    result=[]
    if len(all)==1:
        result.append(all[0])
    else:
        for i in xrange(0,len(all)):
            oldFirst=all[0] #交换当前的头元素
            all[0]=all[i]
            all[i]=oldFirst
            preResult=perm(all[1:])
            for j in xrange(0,len(preResult)):
                result.append(all[0]+preResult[j])
            all[i]=all[0]  #交换后要换回去
            all[0]=oldFirst
    return result

#视元素为字符串列出排列情况，入口函数。如果输入就是字符串，则不要这个函数也行。这里累赘了
def perm(all):
    for i in xrange(0,len(all)):
        all[i]=str(all[i])
    return perm_sub(all)

#打印所有的组合情况
def comb(all):
    for i in xrange(0,len(all)):
        all[i]=str(all[i])
    result=[]
    for i in xrange(1,len(all)+1):
        result.extend( comb_sub(all,i) )
    return result
#打印包含m个元素的组合情况，m个元素的组合数=第一个元素+剩下序列元素的m-个组合数
#如1234，m=2个元素的组合数等于1+[2,3,4](234的m-1组合),2+[3,4](34的m-1组合)，3+[4]
#如1234，m=3个元素的组合数等于1+[23,24,34](234的m-1组合),2+[34](34的m-1组合)
def comb_sub(all,m):
    result=[]
    if m==1:
        result=all
    else:#每次循环将起始位置往后移1，并且保证剩下的元素数大于m-1组合数
        for i in xrange(0,len(all)-(m-1) ):#最后至少要剩下m-1个数，如果剩下的数量都少于要组合的数量就无法组合了
            preResult=comb_sub(all[i+1:],m-1)
            for j in xrange(0,len(preResult)):
                result.append( all[i]+ preResult[j])

    return result





#求all中的m个元素的所有组合情况，要求元素之间的位置间隔不超过d
#按组合情况的求解方法求解，添加组合时与前一个元素的间隔不超过d的条件
#要考虑负负得正的情况，所以直接返回最大不可行
#使用传递下标位置而不是子数组避免复制和内存占用
def wangyi_sub(all,start,m,pre,d):#pre=0表示当前是第一个头,=1表示不是第一个头
    maxResult=-99999999
    minResult=99999999
    if m==1:
        if pre==0:
            maxResult=max(all[start:])
            minResult=min(all[start:])
        else:
            maxResult=max(all[start:start+d])
            minResult=min(all[start:start+d])
    else:
        if pre==0:
            maxLeft=len(all)-start-(m-1)
        else:
            maxLeft=d if d < len(all)-start-(m-1) else len(all)-start-(m-1)
        for i in xrange(start,start+maxLeft):
            preMax,preMin=wangyi_sub(all,i+1,m-1,1,d)
            nowA=all[i] * preMax
            nowB=all[i] * preMin
            if nowA>nowB:
                if nowA>maxResult:maxResult=nowA
                if nowB<minResult:minResult=nowB
            else:
                if nowB>maxResult:maxResult=nowB
                if nowA<minResult:minResult=nowA
    return maxResult,minResult

# def wangyi_sub(all,m,pre,d):
#     result=[]
#     if m==1:
#         if pre==0:
#             result=all
#         else:
#             result=all[:d]
#     else:
#         if pre==0:
#             maxStart=len(all)-(m-1)
#             cuMax=-9999999
#             for i in xrange(0,maxStart):
#                 preResult=wangyi_sub(all[i+1:],m-1,1,d)
#                 for j in xrange(0,len(preResult)):
#                     if all[i] * preResult[j]>cuMax:
#                         cuMax=all[i] * preResult[j]
#             result.append(cuMax)
#         else:
#             maxStart=d if d < len(all)-(m-1) else len(all)-(m-1)
#             for i in xrange(0,maxStart):
#                 preResult=wangyi_sub(all[i+1:],m-1,1,d)
#                 for j in xrange(0,len(preResult)):
#                     result.append( all[i] * preResult[j])
#     return result

# print perm(all)
# print comb(all)

all=[13,-8, -44, 28 ,-37, 49, 50, -34 ,45 ]
print wangyi_sub(all,0,1,0,50)

all=[-41, -5, -10, -31, -44 ,-16, -3 ,-33, -34 ,-35 ,-44 ,-44 ,-25 ,-48, -16 ,-32 ,-37,
			-8 ,-33 ,-30 ,-6 ,-18 ,-26 ,-37 ,-40, -30, -50 ,-32 ,-5 ,-41, -32 ,-12 ,-33 ,-22 ,
			-14 ,-34, -1, -41, -45 ,-8 ,-39 ,-27, -23, -45, -10, -50 ,-34]
print wangyi_sub(all,0,6,0,3)

# all=[7,4,7]
# print wangyi_sub(all,0,2,0,50)

# print wangyi_sub(all,2,0,50)
# print max(wangyi_sub(all,2,0,50))

# all=['1','2','3','4','5','6','7','8','9']
# print wangyi_sub(all,3,0,2)
# print max(wangyi_sub(all,3,0,2))

def wangyiniuke():
    import sys
    n=sys.stdin.readline()
    s=sys.stdin.readline().split(' ')
    for i in xrange(0,len(s)):
        s[i]=int(s[i])
    kd=sys.stdin.readline().split(' ')
    k=int(kd[0])
    d=int(kd[1])
    i=0
    allResult=wangyi_sub(s,k,0,d)
    print max(allResult)
