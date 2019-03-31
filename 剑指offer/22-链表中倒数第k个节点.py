# -*- coding:utf-8 -*-
'''
    链表中倒数第k个节点
==================================
输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，
即链表的尾节点是倒数第1个节点。例如，一个链表有6个节点，从头节点开始，它们的值
依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。链表节点定义如下：
class ListNode(object):
    def __init__(self, val, pNext=None):
        self.val = val
        self.pNext = pNext
'''

class ListNode(object):
    def __init__(self, val, pNext=None):
        self.val = val
        self.pNext = pNext

def KthNodeFromEnd(head, k):
    '''
    思路：由于是单向链表，所以不能通过向后遍历来找到倒数第k个节点，只能从前向
    遍历入手，一种方法是从头遍历到尾，计算链表长度n，再从头遍历到第n-k+1个节点
    该节点就是倒数第k个节点，但是这种方法需要遍历两次链表。另一种只需遍历一次
    链表的方法是用两个指针，一个指针向前走k-1步，第二个指针保持不动；接着从
    第k步开始，第二个指针和第一个指针保持同步前进，直到第一个指针到达链表尾部
    为止。
    注：程序必须考虑健壮性，比如k=0，head=None，n<k的情况。
    扩展：求链表的中间节点，如果链表中的节点总数为奇数，则返回中间节点；如果节点
    总数是偶数，则返回中间两个节点的任意一个。方法是定义两个指针，同时从链表的头
    节点出发，第一个指针一次走两步，第二个指针一次走一步，当第一个指针走到链表的
    尾部时，第二个指针正好在链表中间。
    '''
    if not isinstance(head, ListNode) or head is None or k == 0:
        return None

    pAhead = head
    pBehind = head
    for i in range(k-1):
        if pAhead.pNext is not None:
            pAhead = pAhead.pNext
        else:
            return None
    while pAhead.pNext is not None:
        pAhead = pAhead.pNext
        pBehind = pBehind.pNext
    return pBehind


'''
Test Code Here
'''
def printList(head):
    pNode = head
    while pNode is not None:
        print('The node val is: ', pNode.val)
        pNode = pNode.pNext
    print('PrintList ends.')

def test1():
    p1 = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(3)
    p4 = ListNode(4)
    p5 = ListNode(5)
    p1.pNext = p2
    p2.pNext = p3
    p3.pNext = p4
    p4.pNext = p5
    print('The original List:')
    printList(p1)

    node = KthNodeFromEnd(p1, 2)
    print('The 2th Node Fome End: ', node.val)

def test2():
    p1 = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(3)
    p4 = ListNode(4)
    p5 = ListNode(5)
    p1.pNext = p2
    p2.pNext = p3
    p3.pNext = p4
    p4.pNext = p5
    print('The original List:')
    printList(p1)

    node = KthNodeFromEnd(p1, 1)
    print('The 1th Node Fome End: ', node.val)

def test3():
    p1 = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(3)
    p4 = ListNode(4)
    p5 = ListNode(5)
    p1.pNext = p2
    p2.pNext = p3
    p3.pNext = p4
    p4.pNext = p5
    print('The original List:')
    printList(p1)

    node = KthNodeFromEnd(p1, 5)
    print('The 5th Node Fome End: ', node.val)

def test4():
    p1 = None
    print('The original List:')
    printList(p1)

    node = KthNodeFromEnd(p1, 100)
    print('The 100th Node Fome End: ', node.val)

def test5():
    p1 = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(3)
    p4 = ListNode(4)
    p5 = ListNode(5)
    p1.pNext = p2
    p2.pNext = p3
    p3.pNext = p4
    p4.pNext = p5
    print('The original List:')
    printList(p1)

    node = KthNodeFromEnd(p1, 0)
    print('The 0th Node Fome End: ', node.val)


if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
