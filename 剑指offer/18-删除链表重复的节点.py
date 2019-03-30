# -*- coding:utf-8 -*-
'''
    删除链表重复的节点
=====================
在一个排序的链表中，删除重复的节点。
'''
class ListNode(object):
    def __init__(self, val, pNext=None):
        self.val = val
        self.pNext = pNext

def deleteDuplications(head):
    if not isinstance(head, ListNode):
        return

    preNode = None
    pNode = head
    while pNode is not None:
        needDelete = False
        if pNode.pNext is not None and pNode.val == pNode.pNext.val:
            needDelete = True
        if not needDelete:
            preNode = pNode
            pNode = pNode.pNext
        else:
            value = pNode.val
            pToBeDeleted = pNode
            while pToBeDeleted is not None and pToBeDeleted.val == value:
                pNode = pNode.pNext
                pToBeDeleted = None
                pToBeDeleted = pNode
            if preNode is None:
                head = pNode
            else:
                preNode.pNext = pNode
    return head


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
    p2 = ListNode(3)
    p3 = ListNode(3)
    p4 = ListNode(4)
    p5 = ListNode(4)
    p6 = ListNode(5)
    p1.pNext = p2
    p2.pNext = p3
    p3.pNext = p4
    p4.pNext = p5
    p5.pNext = p6
    print('The original List:')
    printList(p1)


    head = deleteDuplications(p1)
    print('The deleted List: ')
    printList(head)

def test2():
    p1 = ListNode(-1)
    p2 = ListNode(0)
    p3 = ListNode(1)
    p4 = ListNode(2)
    p5 = ListNode(3)
    p1.pNext = p2
    p2.pNext = p3
    p3.pNext = p4
    p4.pNext = p5
    print('The original List:')
    printList(p1)


    head = deleteDuplications(p1)
    print('The deleted List: ')
    printList(head)

def test3():
    p1 = ListNode(1)
    p2 = ListNode(1)
    p3 = ListNode(1)
    p4 = ListNode(1)
    p5 = ListNode(3)
    p1.pNext = p2
    p2.pNext = p3
    p3.pNext = p4
    p4.pNext = p5
    print('The original List:')
    printList(p1)


    head = deleteDuplications(p1)
    print('The deleted List: ')
    printList(head)

def test4():
    p1 = ListNode(1)
    p2 = ListNode(1)
    p3 = ListNode(1)
    p4 = ListNode(1)
    p5 = ListNode(1)
    p1.pNext = p2
    p2.pNext = p3
    p3.pNext = p4
    p4.pNext = p5
    print('The original List:')
    printList(p1)


    head = deleteDuplications(p1)
    print('The deleted List: ')
    printList(head)

def test5():
    p1 = ListNode(1)
    p2 = ListNode(2)
    p1.pNext = p2
    print('The original List:')
    printList(p1)


    head = deleteDuplications(p1)
    print('The deleted List: ')
    printList(head)

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()

