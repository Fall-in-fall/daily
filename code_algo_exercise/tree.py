# -*- encoding:utf-8 -*-
class Node:
    left = None ; right = None ; val = 0

#循环遍历二叉树: 主要思想是用栈记录遍历路径，方便回退按某顺序遍历下一个节点
    # 前序在循环中，对于每一个节点都一直往左走把经过节点入栈，然后依次取栈将其右子节点入栈，对右节点继续执行上述操作
def circ_preorder(t):
    if t==None:return
    rec = [t]
    node = t
    while len(rec)!=0:
        while node!=None: # 遍历并保存最左路径
            print node
            node = node.left
            rec.append(node)
        node = rec.pop()
        if node.right!=None: # 取出遍历过的上一个节点的右子节点加入栈，下一次循环取出的就是这个节点
            rec.append(node.right)

def circ_midorder(t): #中序遍历，先往左走到底，然后取出输出，下一次对右子节点进行相同操作
    if t==None:return
    rec = [t]
    node = t
    while len(rec)!=0:
        while node!=None: # 保存最左路径
            node = node.left
            rec.append(node)
        node = rec.pop() # 当前已是最左，读取输出
        print node
        if node.right != None:
            node = node.right # 下一次对右子节点进行遍历

# 重建二叉树-p55
    #根据前序和中序

# 判断B是不是A的子树:前序遍历找到相同root，然后从root递归往下判断每一个子节点是否都相同.（二叉树）
def isSubTree(a,b):
    if a == None or b == None:
        return False
    if a.val == b.val:
        return isAllSame(a,b)
    else:
        return isSubTree(a.left,b) or isSubTree(a.right,b)
def isAllSame(a,b):
    if b is None:
        return True
    elif a is None:
        return False
    elif a.val==b.val:
        sameLeft = isAllSame(a.left,b.left)
        sameRight = isAllSame(a.right,b.right)
        if sameLeft and sameRight:
            return True
        else:
            return False
    else:
        return False

#二叉树镜像：递归前序遍历，每一步操作是交换左右子女，

# 二叉树中和为某值的路径：前序遍历，使用一个栈存储当前已有路径，如果在某一节点满足要求则加入当前点并打印路径(或存入容器)，
        # 否则如果和已经大于返回False，小于则继续传递

# 两个树节点的最近祖先
# 对于二叉搜索树，则找到第一个值在两节点中间的节点就是最近祖先
# 对于带父指针，则可以向上回溯，看作找两个链表的公共节点
# 一般树，做两次遍历分别找到两个节点，并记录遍历路径，然后仍然转化为两个链表的公共节点问题。使用递归遍历，多加一个栈参数即可。

# 二叉树的非递归遍历：一般是两层循环，根据遍历的顺序，用栈记录要回退的路径

# 二叉树深度：后续遍历
def depth(root):
    if root==None:return 0
    nleft,nright = depth(left),depth(right)
    return (nleft+1) if nleft>nright else (nright+1)

# 判断是不是平衡二叉树-p209(任一节点左右质数深度不超过1)：前序遍历的方式会产生重复，使用后序遍历(先)，
        # 传递一个当前深度(前面已经过的深度)的参数。从最底层往上返回判断是否平衡

