# -*- coding:utf-8 -*-
'''
    链表中环的入口节点
=======================
如果一个链表中包含环，如何找出环的入口节点？
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

def entryNodeFromLoop(head):
    '''
    思路：首先需要判断一个链表中是否包含环，如果不包含环，返回None；如果包含环，
    返回环的入口节点。那么如何判断链表中是否包含环呢？方法是定义两个指针p1和p2，
    让p1一次移动两部，p2一次移动一步，当p1追上p2时(p1==p2)，则链表中含有环，
    返回p1。
    接下来则需要找出环的入口节点，首先计算环的节点数k，利用上一步返回的指针p1，
    使用另外一个指针p3，p3从p1位置出发，一次移动一步，直到p3移动回p1为止，得到
    移动的步数k。在得到环的总节点数之后，重新定义两个指针p1和p2，p1先移动k步，
    p2保持不动；接下来p2和p1保持同步，一次移动一步，直到它们相遇。它们相遇的节点
    正好是环的入口节点。
    '''
    def meetingNode(head):
        if head is None:
            return None

        pSlow = head
        if pSlow.pNext is not None:
            pSlow = pSlow.pNext
        else:
            return None
        pFast = pSlow.pNext
        while pFast is not None and pSlow is not None:
            if pFast == pSlow:
                return pFast

            pSlow = pSlow.pNext
            pFast = pFast.pNext
            if pFast is not None:
                pFast = pFast.pNext
        return None

    if not isinstance(head, ListNode) or head is None:
        return None

    meetNode = meetingNode(head)
    if meetNode is None:
        return None

    nodesInLoop = 1
    pNode = meetNode
    while pNode.pNext != meetNode:
        nodesInLoop += 1
        pNode = pNode.pNext

    pAhead = head
    for i in range(nodesInLoop):
        pAhead = pAhead.pNext

    pBehind = head
    while pBehind != pAhead:
        pAhead = pAhead.pNext
        pBehind = pBehind.pNext

    return pAhead



'''
Test Code Here
'''
def test1():
    p1 = ListNode(1)
    p1.pNext = p1

    node = entryNodeFromLoop(None)
    print('The Entry Node of Loop: ', node.val)

def test2():
    p1 = ListNode(1)
    p1.pNext = p1

    node = entryNodeFromLoop(p1)
    print('The Entry Node of Loop: ', node.val)

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
    p5.pNext = p3

    node = entryNodeFromLoop(p1)
    print('The Entry Node of Loop: ', node.val)

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
    p5.pNext = p1

    node = entryNodeFromLoop(p1)
    print('The Entry Node of Loop: ', node.val)

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
    p5.pNext = p5

    node = entryNodeFromLoop(p1)
    print('The Entry Node of Loop: ', node.val)


if __name__ == '__main__':
    # test1()        # The expected value should be None
    # test2()        # The expected value should be 1
    # test3()        # The expected value should be 3
    # test4()        # The expected value should be 1
    # test5()        # The expected value should be 5