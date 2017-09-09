# -*- encoding:utf-8 -*-
#------------------------------------
 #背包问题
#------------------------------------

#背包问题 - 假设sizeArr(宝石大小)有序,valueArr 对应size的宝石的价值。假设各个size的宝石不限量。解法同上
def maxValuePackage_many_recursive(sizeArr,valueArr,maxSize):
    if maxSize == 0:
        return 0,{}
    if maxSize<sizeArr[0]:
        return -1,{}

    if maxSize>sizeArr[-1]:
        shortList=sizeArr
    else: #(假设输入size按升序排列，简单优化只取部分宝石，可以去掉
        shortList = []
        for s in xrange(len(sizeArr)-1,-1,-1):
            if sizeArr[s] <= maxSize:
                shortList = sizeArr[0:s+1]
                break
    maxValue = 0
    sizeIndexDict = {}
    maxIndex = -1
    isTheMaxInNew = False
    for i in xrange(0,len(shortList)):
        lastValue,lastDict = maxValuePackage_many_recursive(shortList,valueArr,maxSize-shortList[i])
        findNew = False
        if lastValue !=-1:
            cuValue =  valueArr[i] + lastValue
            findNew = True
        else:
            cuValue = valueArr[i]
        if cuValue > maxValue: #每次都进行一次设置，从而保留最后设置的值。判断最大值是不是新加入一个宝石后得到的。
            isTheMaxInNew = True if findNew else False
            maxValue = cuValue
            maxIndex = i
            sizeIndexDict = lastDict
    if isTheMaxInNew:
        if not sizeIndexDict.has_key(maxIndex):
            sizeIndexDict[maxIndex]=0
        sizeIndexDict[maxIndex]+=1
    print maxIndex,maxValue
    return maxValue,sizeIndexDict

#背包问题 - 递归 - 宝石是唯一的。
def maxValuePackage_recursive(sizeArr,valueArr,maxSize):
    if maxSize == 0:
        return 0,{}
    if maxSize<sizeArr[0]:
        return -1,{}

    if maxSize>sizeArr[-1]:
        shortList=sizeArr
    else: # 这里只是简单的加一步优化，假设候选宝石排序，对于输入的maxSize小于最大候选的只选取有用的部分。
        shortList = []
        for s in xrange(len(sizeArr)-1,-1,-1):
            if sizeArr[s] <= maxSize:
                shortList = sizeArr[0:s+1]
                break
    maxValue = 0
    selectSizeDict = {}
    choseSize = -1
    isTheMaxInNew = False
    for i in xrange(0,len(shortList)):
        leftShortList = shortList[:]
        leftShortList.pop(i)
        leftValueList = valueArr[:]
        leftValueList.pop(i)
        lastValue,lastDict = maxValuePackage_recursive(leftShortList,leftValueList,maxSize-shortList[i])
        if lastValue !=-1:
            cuValue =  valueArr[i] + lastValue
        else:
            cuValue = valueArr[i]
        if cuValue > maxValue: #每次都进行一次设置，从而保留最后设置的值。判断最大值是不是新加入一个宝石后得到的。
            maxValue = cuValue
            choseSize = shortList[i]
            selectSizeDict = lastDict
    if not selectSizeDict.has_key(choseSize):
        selectSizeDict[choseSize]=0
    selectSizeDict[choseSize]+=1
    #print shortList,maxValue
    return maxValue,selectSizeDict

# 背包问题 - 宝石是唯一的,循环动态规划解法。
# 因为宝石是唯一的，当判断放入一个宝石是否值得时，只需要在1,2中判断
# 1 假设选择当前宝石，放入这个宝石后的剩余体积所能获得的最大价值(前面i-1个宝石所能获得的)加上这个宝石的价值
# 2 不放入这个宝石，取得i-1个宝石在当前体积下能获得的最大价值
# 所以在这里的依赖是 有第i个宝石的(能否构成更大价值)情况依赖于i-1个宝石在j-v(i)体积时的最大价值情况，
# (需要先知道各个体积下的最大价值) 同时剩余体积j的情况依赖于剩余体积j-j-v(i)的情况
# 所以外层循环宝石，内层循环体积
#      (这里跟宝石价值排列是没有关系的，每加入一个新宝石参与考虑时，
#       都会依据前面计算好的最大价值情况对各个最大价值进行更新)
# 状态转移为 d(i, j)=max{ d(i-1, j), d(i-1,j-V[i-1]) + W[i-1] }

# 内层(对体积的)循环是逆序的，
# 递推关系是
def maxValuePackage_dp(sizeArr,valueArr,maxSize):

    allTotalValue = [  ]  #注意python的语法中 [x]*n = [x,x,x],如果x不是基本类型，则拷贝的是引用，对x的修改会反映到所有列表内的x身上，所以会导致问题
    for i in xrange(0,len(sizeArr)):
        allTotalValue.append( [0] * (maxSize + 1) )
        #iTotalValue += sizeArr[i-1] if i >0 else 0
        for j in xrange(1,maxSize+1): # 此处可以按递减顺序更新，使用一维数组d，对每一步 d(i-1, j-V)变为d(j-V)， d(i-1, j)变为d(j)
            leftSize = j - sizeArr[i]
            if leftSize<0:
                allTotalValue[i][j] = allTotalValue[i-1][j] if i>0 else 0
            else:
                afterAdd = allTotalValue[i-1][leftSize]+valueArr[i] if i>0 else valueArr[i]
                if afterAdd > allTotalValue[i-1][j]:
                    allTotalValue[i][j] = afterAdd
                else:
                    allTotalValue[i][j] = allTotalValue[i-1][j]
    selectList = []
    c=maxSize
    for i in xrange(len(sizeArr)-1,-1,-1):
        last = allTotalValue[i-1][c] if i >0 else 0
        if allTotalValue[i][c]>last:
            selectList.append(sizeArr[i])
            c -= sizeArr[i]

    return allTotalValue[len(sizeArr)-1][maxSize],selectList

if __name__ == '__main__':
    print 'a ',maxValuePackage_recursive([3, 4, 5], [12, 10, 20], 10)
    print 'b ',maxValuePackage_dp([3,4,5],[12,10,20],10)