# -*- encoding:utf-8 -*-
import sys
#------------------------------------
 #最xx子序列
#------------------------------------
# 给定一个数列，长度为N，
# 求这个数列的最长上升（递增）子数列（LIS）的长度.
# 以 1 7 2 8 3 4 为例。
# 这个数列的最长递增子数列是 1 2 3 4，长度为4；
# 次长的长度为3， 包括 1 7 8; 1 2 3 等.
# d(i) = max(前面所有比i小的数的最长子序列长度)+1
def LIS( arr ):
    allMaxLen = [0]*len(arr)
    maxLength = 0
    maxIndex =0
    for i in xrange(0,len(arr)):
        isFoundLess = False
        theMax=0
        for j in xrange(i-1,-1,-1):
            if arr[j]<arr[i] and arr[j]>theMax:
                theMax = allMaxLen[j]
                break
        allMaxLen[i]= theMax+1
        if allMaxLen[i]>maxLength:
            maxLength=allMaxLen[i]
            maxIndex = i
    print allMaxLen
    return maxLength,maxIndex


# 平面上有N*M个格子，每个格子中放着一定数量的苹果。# 从左上角的格子开始，
# 每一步只能向下走或是向右走，每次走到一个格子上就把格子里的苹果收集起来，
# 最多能收集到多少个苹果
def maxApple(arr):
    allMax = [ele[:] for ele in arr]
    m = len(arr)
    n = len(arr[0])
    for i in xrange(0,m):
        for j in xrange(0,n):
            left = allMax[i][j-1] if j>0 else 0
            up = allMax[i-1][j] if i>0 else 0
            allMax[i][j] = max([left, up])+arr[i][j]
    return allMax[m-1][n-1]


#一组数中和最大的子序列之和(要输出子序列思想类似，但是很麻烦，需要各种if else判断)
# 记录当前位置时的最大和 = max(last+self,self),所以只需要判断前一个是大于0还是小于0就可以了
def maxSubSum( arr ):
    lastSum = arr[0]
    cuMax = lastSum
    for i in xrange(1,len(arr)):
        if lastSum<0:
            lastSum=arr[i]
        else:
            lastSum=arr[i]+lastSum
        if lastSum>cuMax:
            cuMax=lastSum
    return cuMax

#一组数中乘积最大的子序列乘积(要输出子序列思想类似，但是很麻烦，需要各种if else判断)
def maxSubMultiply( arr ):
    def maxAndMinInArr(valueArr ):
        maxValue = valueArr[0]
        minValue = valueArr[0]
        for i in xrange(1,len(valueArr)):
            if valueArr[i]>maxValue:
                maxValue = valueArr[i]
            elif valueArr[i]<minValue:
                minValue=valueArr[i]
        return maxValue,minValue
    posValue = [0]*len(arr)
    negValue = [0]*len(arr)
    if arr[0]>0:
        posValue[0] = arr[0]
    else:
        negValue[0] = arr[0]
    cuMax = arr[0]
    for i in xrange(1,len(arr)):
        a = posValue[i-1]
        b = negValue[i-1]
        c = arr[i]
        tempMax,tempMin = maxAndMinInArr([a*c,b*c,c]) #
        if tempMax>0:
            posValue[i]=tempMax
            if tempMax>cuMax:
                cuMax=tempMax
        if tempMin<0:
            negValue[i]=tempMin
    print arr
    print '\t'.join(map(str,posValue))
    print '\t'.join(map(str,negValue))
    return cuMax


#------------------------------------
 #凑够x元需要最少硬币数
#------------------------------------

# 有面值为1元、3元和5元(设面值为s)的硬币若干枚，凑够x元最少的硬币,
# 硬币问题的依赖是 x元最少所需硬币数依赖于x-s元
# 循环解法，要依次遍历获取每一个子步的解(包括找不到的情况)，如果最小面值>
# return (最小硬币数(0或-1为找不到。)，最小所需各面值硬币数量字典)
def minCoinNum(x,coinAll = [3, 5]):
    allMin = [0] * (x + 1)
    minCoinListDict = {0: {}}
    for i in xrange(1, x + 1, 1):
        minCoinListDict[i] = {}
        if i < coinAll[0]:
            allMin[i] = -1
        else:
            if i >= coinAll[-1]:
                sl = coinAll
            else: #(假设输入面值按升序排列，简单优化只取部分硬币，可以去掉
                for index in xrange(len(coinAll) - 1, -1, -1):
                    if coinAll[index] <= i:
                        sl = coinAll[0: index + 1]
                        break
            currentMin = sys.maxint
            minCoin = -1
            findMin = False
            for coin in sl:
                lastMin = allMin[i - coin]
                if lastMin >= 0:
                    current = allMin[i - coin] + 1
                    if current < currentMin:
                        currentMin = current
                        minCoin = coin
                        findMin = True
            if findMin:
                minCoinListDict[i].update(minCoinListDict[i - minCoin])
                if not minCoinListDict[i].has_key(minCoin):
                    minCoinListDict[i][minCoin] = 0
                minCoinListDict[i][minCoin] += 1
                allMin[i] = currentMin
            else:
                allMin[i] = -1
    return allMin[x], minCoinListDict[x]

# 递归版最小硬币数,返回同上（此递归的解法不是动态规划。
# 递归可以看做自顶向下分裂一颗树，每个节点都是一次计算。实际上递归的计算量可能会比动态规划高，因为有的节点的计算可能是重复的
# 比如 17->3->5->9,17->5->3->9，凑够9元所需硬币被计算了两次，没有得到复用。当重复较少时，递归的总计算量是小于动态规划的。
# 递归与动态规划不一定谁更高效(节点计算重复少的时候递归会好一点点，这取决于数据)，但是总整体角度来讲，动态规划的效率更高。
# 而动态规划的核心思想之一就是记忆（或者记录）来避免对重复子问题进行求解，但是它没有避免对不必要子问题进行求解(比如硬币只有3,5却计算了很多如 1,2,4,6,7 这样的不必要子问题)。
# 所以终极解法是结合循环动态规划与递归方法的记忆递归，在递归的过程中保留已有解，遇到重复计算的时候可以直接取出。实现避免不必要子问题与避免重复解两重效果。
def minCoinNum_recursive(x,coinAll = [3, 5]):
    if x==0: return 0,{}
    if x<coinAll[0]: return -1,{}

    if x> coinAll[-1]: sl = coinAll
    else:
        for index in xrange(len(coinAll)-1,-1,-1):
            if coinAll[index]<=x:
                sl = coinAll[0: index + 1]
                break
    currentMin = sys.maxint
    findMin = False
    minCoin = -1
    minCoinList={}
    for coin in sl:
        lastMin,lastMinCoinList = minCoinNum_recursive(x-coin,sl)
        if lastMin != -1:
            current = lastMin+1
            if current<currentMin:
                currentMin = current
                minCoin = coin
                minCoinList = lastMinCoinList
                findMin = True
    if findMin:
        if not minCoinList.has_key(minCoin):
            minCoinList[minCoin]=0
        minCoinList[minCoin]+=1
        return currentMin,minCoinList
    else:
        return -1,{}

if __name__ =='__main__':
    # print minCoinNum_recursive(5)
    # print minCoinNum(5)

    # print maxSubMultiply([1,0,-1,2,3,-5,-2])
    # print maxSubMultiply([0,0.2,3,-1,-7,-5,6,-3,-0.9,8])

    # print maxSubSum([1,0,-1,2,3,-5,-2])
    # print maxSubSum([0, 0.2, 3, -1, -7, -5, 6, -3, -0.9, 8])

    print LIS([1,7,8,2,3,4])