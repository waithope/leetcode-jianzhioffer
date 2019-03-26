# -*- coding:utf-8 -*-
'''
    删除链表的节点
=====================
在O(1)时间内删除链表节点。
给定单向链表的头指针和一个节点指针，定义一个函数在O(1)时间内删除该节点。
'''

class ListNode(object):
    def __init__(self, val, pNext=None):
        self.val = val
        self.pNext = pNext

def deleteNode(head, pToBeDeleted):
    '''
    单向链表没有指向前驱节点的指针，要在O(1)时间内删除指定节点，可以通过将
    指定节点i的值用该节点的下一个节点j的值进行覆盖，然后将该节点指向到j节点
    的下一个节点。
    注：有两种情况要特别注意，第一种是整个链表只有一个节点，第二种是要删除的
    节点位于链表的末尾。
    '''
    if (not isinstance(head, ListNode)
        or not isinstance(pToBeDeleted, ListNode)):
        return

    if pToBeDeleted.pNext is not None:
        pNode = pToBeDeleted.pNext
        pToBeDeleted.val = pNode.val
        pToBeDeleted.pNext = pNode.pNext
    elif head == pToBeDeleted:
        head = None
    else:
        pNode = head
        while pNode.pNext != pToBeDeleted:
            pNode = pNode.pNext
        pNode.pNext = pToBeDeleted.pNext
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


    head = deleteNode(p1, p3)
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


    head = deleteNode(p1, p5)
    print('The deleted List: ')
    printList(head)

def test3():
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


    head = deleteNode(p1, p1)
    print('The deleted List: ')
    printList(head)

def test4():
    p1 = ListNode(-1)
    print('The original List:')
    printList(p1)

    head = deleteNode(p1, p1)
    print('The deleted List: ')
    printList(head)


if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
