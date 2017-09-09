# -*- encoding:utf-8 -*-
class Node:
    data=0
    next=None
    def __init__(self,data):
        self.data=data

#O(1)时间删除节点：
    # 输入节点指针，将下一个节点的内容复制到该节点上，然后删除下一节点
# 合并两个有序列表：
    #递归过程，输入两个头，返回较大的作为头。
def merge(node1,node2):
    # 判空
    theHead = None
    if node1.val>node2/val:
        theHead = node1
        theHead.next = merge(node1.next,node2)
    else:
        heHead = node2
        theHead.next = merge(node1, node2.next)
    return theHead

# 反转
def reverse(head):
    if head is None or  head.next is None:
        return head
    cuNode=head
    prev = None
    while cuNode is not None:
        cuNext = cuNode.next
        cuNode.next=prev
        prev=cuNode
        cuNode=cuNext
    return prev

# 去重链表重复(数据值)元素 https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
def removeDuplicates(head):
    #有序
    cuNode = head
    while node is not None and node.next is not None:
        cuNode=node
        while cuNode is not None and cuNode.next is not None and cuNode.data == cuNode.next.data :
            cuNode=cuNode.next
        if cuNode is not node:
            node.next = cuNode.next
        node = node.next

    # 有序2
    cuNode = head
    while cuNode is not None and cuNode.next is not None:
        if cuNode.data == cuNode.next.data:
            cuNode.next = cuNode.next.next
        else:
            cuNode = cuNode.next

    #非有序，用set，略
    # all = set()

    #不保留，删除所有有重复的元素
    newNode = Node()
    newNode.next = head
    node = newNode
    while node is not None and node.next is not None:
        cuNode = node
        while cuNode is not None and cuNode.next.next is not None and cuNode.data==cuNode.next.data :
            cuNode = cuNode.next
        if cuNode is not node:
            node.next = cuNode.next
        else:
            node = cuNode.next

#把小于x的放在前面，其余放在后面 https://leetcode.com/problems/partition-list/
def partionList(head,x):
    #定义两个头，把小于x的挂一个，大于x的挂一个，最后合并两个链表即可
    # 略...
    # 一下是定义一个头的方法，不实用
    newNode = Node(x-1)
    newNode.next = head
    node = newNode
    while node.next is not None:
        cuNode = node
        while cuNode.next is not None and cuNode.next.data>=3:
            cuNode = cuNode.next
        if cuNode is not node:
            # 设0->1->4->3->2->5->2
            # 第一次，遍历到cuNode = 3，则变为1指向2，2指向4，3指向5
            oriNodeNext = node.next
            oriCuNextNext = cuNode.next.next

            node.next = cuNode.next
            node.next.next = oriNodeNext

            cuNode.next = oriCuNextNext
# 反转指定位置部分的链表(下标从1开始) https://leetcode.com/problems/reverse-linked-list-ii/
def reversePart(head,m,n):
    if m == n:
        return head
    count = 1
    node = head
    prev = None
    while count != m:
        prev = node
        node = node.next
        count += 1
    before = prev
    start = node
    isToEnd = False
    while count != n + 1:
        if node is None:
            isToEnd = True;
            break
        oriNext = node.next
        node.next = prev
        prev = node
        node = oriNext
        count += 1
    end = node
    if m == 1:
        start.next = end
        return prev
    else:
        before.next = prev
        start.next = end
        return head

# 对链表排序O(nlog n)，O(1)空间复杂度  https://leetcode.com/problems/sort-list/description/
def sortList():
    pass

# 两个链表的第一个公共节点
# 因为第一个公共节点之后都是相同节点，可以借助栈进行倒序遍历。将两个链表分别压入两个栈，然后每次弹出两个栈顶直到弹出的元素不一样，则上一次就是第一个公共节点
# 不用栈的话，可以先得到两个链表的长度，然后对于长链表先走几步到长度一致，然后在一起往前走直到出现相同节点。












