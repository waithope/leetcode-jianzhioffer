# -*- coding:utf-8 -*-
'''
    合并两个排序的链表
========================
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
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

def mergeList(head1, head2):
    if head1 is None:
        return head2
    elif head2 is None:
        return head1

    pMergedHead = None
    if head1.val <= head2.val:
        pMergedHead = head1
        pMergedHead.pNext = mergeList(head1.pNext, head2)
    else:
        pMergedHead = head2
        pMergedHead.pNext = mergeList(head1, head2.pNext)

    return pMergedHead


def mergeList_iteratively(head1, head2):
    dummyHead = ListNode(0)
    current = dummyHead
    while head1 is not None and head2 is not None:
        if head1.val <= head2.val:
            current.pNext = head1
            head1 = head1.pNext
            current = current.pNext
        else:
            current.pNext = head2
            head2 = head2.pNext
            current = current.pNext
    if head1 is not None:
        current.pNext = head1
    if head2 is not None:
        current.pNext = head2
    return dummyHead.pNext


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
    p6 = ListNode(6)
    p1.pNext = p3
    p2.pNext = p4
    p3.pNext = p5
    p4.pNext = p6
    print("The first list is: ");
    printList(p1)
    print("The second list is: ")
    printList(p2)
    pMergedHead = mergeList_iteratively(p1, p2)
    print('The Merged List is: ')
    printList(pMergedHead)

def test2():
    p1 = ListNode(1)
    p2 = ListNode(1)
    p3 = ListNode(3)
    p4 = ListNode(3)
    p5 = ListNode(5)
    p6 = ListNode(5)
    p1.pNext = p3
    p2.pNext = p4
    p3.pNext = p5
    p4.pNext = p6
    print("The first list is: ");
    printList(p1)
    print("The second list is: ")
    printList(p2)
    pMergedHead = mergeList_iteratively(p1, p2)
    print('The Merged List is: ')
    printList(pMergedHead)

def test3():
    p1 = ListNode(1)
    p2 = ListNode(2)
    print("The first list is: ");
    printList(p1)
    print("The second list is: ")
    printList(p2)
    pMergedHead = mergeList_iteratively(p1, p2)
    print('The Merged List is: ')
    printList(pMergedHead)

def test4():
    p1 = ListNode(1)
    p3 = ListNode(3)
    p5 = ListNode(5)
    p1.pNext = p3
    p3.pNext = p5
    print("The first list is: ");
    printList(p1)
    print("The second list is: ")
    p2 = None
    printList(p2)
    pMergedHead = mergeList_iteratively(p1, p2)
    print('The Merged List is: ')
    printList(pMergedHead)

def test5():
    p1 = None
    p2 = None
    print("The first list is: ");
    printList(p1)
    print("The second list is: ")
    printList(p2)
    pMergedHead = mergeList_iteratively(p1, p2)
    print('The Merged List is: ')
    printList(pMergedHead)

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()