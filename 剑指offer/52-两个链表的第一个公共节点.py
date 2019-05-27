# -*- coding:utf-8 -*-
'''
    两个链表的第一个公共节点
==============================
输入两个链表，找出它们的第一个公共节点。
链表节点定义如下：
class ListNode(object):
    def __init__(self, val, pNext=None):
        self.val = val
        self.pNext = pNext
'''
class ListNode(object):
    def __init__(self, val, pNext=None):
        self.val = val
        self.pNext = pNext

def findFirstCommonNode(pHead1, pHead2):
    '''
    思路：从链表节点的定义可以看出，这两个链表都是单向链表。如果两个单向链表有
    公共节点的话，那么这两个链表从某一节点开始，它们的pNext都指向同一个节点，
    一直到各自链表的尾部为止。有两种方法可以找到公共节点，第一种是将链表各自压入
    对应的栈中，两个栈的栈顶就是各自链表的末尾节点。接着同时进行弹出操作，并比较
    弹出的两个节点是否相同，当不相同时，前一个节点就是公共节点。第二种是通过遍历
    链表得到各自链表的长度，然后先在较长的链表上走一定的步数，步数为两个链表长度的
    差，然后同步比较下一个节点是否相同，如果相同，则找到了两个链表的公共节点。
    '''
    def getListLength(pHead):
        length = 0
        pNode = pHead
        while pNode is not None:
            pNode = pNode.pNext
            length += 1
        return length

    if (not isinstance(pHead1, ListNode) or pHead1 is None
        or not isinstance(pHead2, ListNode) or pHead2 is None):
        return

    length1 = getListLength(pHead1)
    length2 = getListLength(pHead2)
    diffLength = length1 - length2
    pListHeadLong = pHead1
    pListHeadShort = pHead2
    if length1 < length2:
        pListHeadLong = pHead2
        pListHeadShort = pHead1
        diffLength = length2 - length1
    for i in range(diffLength):
        pListHeadLong = pListHeadLong.pNext

    while (pListHeadLong is not None
           and pListHeadShort is not None
           and pListHeadLong != pListHeadShort):
           pListHeadLong = pListHeadLong.pNext
           pListHeadShort = pListHeadShort.pNext

    pListCommonNode = pListHeadLong
    return pListCommonNode


'''
Test Code Here
'''
def printList(head):
    pNode = head
    while pNode is not None:
        print('The node val is: ', pNode.val)
        pNode = pNode.pNext
    print('PrintList ends.')

# 第一个公共结点在链表中间
# 1 - 2 - 3 \
#            6 - 7
#     4 - 5 /
def test1():
    p1 = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(3)
    p4 = ListNode(4)
    p5 = ListNode(5)
    p6 = ListNode(6)
    p7 = ListNode(7)
    p1.pNext = p2
    p2.pNext = p3
    p3.pNext = p6
    p4.pNext = p5
    p5.pNext = p6
    p6.pNext = p7

    node = findFirstCommonNode(p1, p4)
    if p6 == node:
        print('Test1 is passed')
    else:
        print('Test1 is not passed')

# 没有公共结点
# 1 - 2 - 3 - 4

# 5 - 6 - 7
def test2():
    p1 = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(3)
    p4 = ListNode(4)
    p5 = ListNode(5)
    p6 = ListNode(6)
    p7 = ListNode(7)
    p1.pNext = p2
    p2.pNext = p3
    p3.pNext = p4
    p5.pNext = p6
    p6.pNext = p7

    node = findFirstCommonNode(p1, p5)
    if node is None:
        print('Test2 is passed')
    else:
        print('Test2 is not passed')

# 公共结点是最后一个结点
# 1 - 2 - 3 - 4 \
#                7
#         5 - 6 /
def test3():
    p1 = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(3)
    p4 = ListNode(4)
    p5 = ListNode(5)
    p6 = ListNode(6)
    p7 = ListNode(7)
    p1.pNext = p2
    p2.pNext = p3
    p3.pNext = p4
    p4.pNext = p7
    p5.pNext = p6
    p6.pNext = p7

    node = findFirstCommonNode(p1, p5)
    if node == p7:
        print('Test3 is passed')
    else:
        print('Test3 is not passed')


# 公共结点是第一个结点
# 1 - 2 - 3 - 4 - 5
# 两个链表完全重合
def test4():
    p1 = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(3)
    p4 = ListNode(4)
    p5 = ListNode(5)
    p1.pNext = p2
    p2.pNext = p3
    p3.pNext = p4
    p4.pNext = p5

    node = findFirstCommonNode(p1, p1)
    if node == p1:
        print('Test4 is passed')
    else:
        print('Test4 is not passed')


if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()