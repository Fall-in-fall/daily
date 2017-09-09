# -*- encoding:utf-8 -*-
#前序、中序、后序、层次遍历及非递归实现 查找、统计个数、比较、求深度的递归实现
#http://blog.csdn.net/fansongy/article/details/6798278/

# 二分查找
def binSearch(arr,x):
    left,right = 0,len(arr)-1
    mid = int(left+right)/2
    while left<=right: #这里必须<=
        if arr[mid] >x :
            right = mid-1 #必须记得要-1，不然循环无法结束(因为循环条件里有=)
        elif arr[mid] < x:
            left = mid+1
        else:
            return mid
        mid = int(left+right)/2
    return -1

# 旋转数组的最小树枝(被旋转的排序数组的二分查找)-p66：

# 按螺旋顺序打印矩阵：把矩阵看做若干个圈，每次打印一圈(输入能表示圈的位置信息)，递归执行。剑指offer129。本代码自己实现未验证
# 注意在于当矩阵的行列数不同时，最内圈的情况不同。需要判断。
# 行列皆偶，则最内扔是圈。奇数行，则最内圈是一行，同样奇数列则最内圈是一列。奇数方阵最内圈则是一格
# 下面的圈是由 [left:right+1][up], [up-1:down][right], [right-1:left+1][down], [down-1:up][left]，四条线组成，注意每条线的位置长短
# 如果取线的方法不同则位置判断不同，需要注意
# left.up-----right.up
# left.down---right.down
def spiralMatrix( matrix ): #设是一个二维数组，每个元素存一行
    printCircle(matrix,0,len(matrix[0]),0,len(matrix))
def printCircle(matrix, left, up, right,down): #如果是方阵可以简化为两个参数来表示圈
    if left <= right : #因为取的最上方这条线最长，所以在这里用等于，可以打印一格的情况
        print [matrix[i][up] for i in range(left,right+1) ]
    if up > down:
        print [matrix[right][i] for i in range(up+1,down) ]

    if left<right and up>down:
        print [matrix[i][down] for i in range(right-1,left+1,-1) ]
        print [matrix[left][i] for i in range(down-1,up,-1) ]
    else:
        return
    printCircle(matrix,left+1,up-1,right-1,down+1)

#给定一个压栈序列，判断一个出栈序列是否正确
# 剑指offer132-22题：初始空栈。遍历出栈序列，如果弹出数字刚好是栈顶数字，则弹出，
# 否则执行压栈直到遇到该数字被压入为止。如果所有某数字在所以数字入栈后仍未遇到，则False

# 数组中的逆序对数：利用归并排序的思想，先分割成最小单位，然后在合并的过程(两组之间逐一比较元素)中统计逆序数。
# 即先把数组分隔成子数组，先统计子数组内部逆序对数，在统计相邻两个子数组间能构成的逆序对数。统计完后要进行排序
    # (顺序排，顺序排序好的部分代表已经统计完逆序对的部分，后面再合并时统计逆序对就会避免重复-前面原本逆序的都已经顺序)

# 排序数组中某数字出现的次数-38-p204 o(logn)：利用二分查找，首先找到这个数。然后分两种情况，可以使用递归实现。
# 一个是向前找到第一次出现(如果k前面还是k，则继续向前二分)，另一个向后找到最后一次出现(如果k后面还是k，则继续向后二分)。

# 数组中只出现一次的数(其他都出现了一次)-p211：一个数对同一个数进行两次异或操作，原数保持不变。
    # 依次对数组中的数进行异或，得到的最后结果是只出现一次的数之间的异或结果m，如果只有一个这样的数则直接返回，
    # 如果有x个，则这x个数不可能同一位上都为1，即可以用m的二进位来进行区分。类似于错误编码的一对多分类。
    # m的某一位是否为1，可以用来分开x的一个数与其他数，并且那些相同的数在该位上肯定相同，所以按照该为划分肯定能把成对出现的数划分到一个组
    # 利用这种方法，可以将只出现一次的数分到各个组，然后在组内再进行一遍异或操作从而提取出这个数

#

if __name__ =='__main__':
    print binSearch([1,2,5,6,45,77],2)