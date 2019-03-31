# -*- coding:utf-8 -*-
'''
    反转链表
===============
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
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

def reverseList(head):
    '''
    提示：需要定义3个指针，分别记录当前节点的上一个节点，当前节点，当前节点的下一个节点。
    '''
    if not isinstance(head, ListNode) or head is None:
        return None

    preNode = None
    nextNode = None
    currentNode = head
    while currentNode is not None:
        nextNode = currentNode.pNext
        currentNode.pNext = preNode
        preNode = currentNode
        currentNode = nextNode
    head = preNode
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
    p2 = ListNode(2)
    p3 = ListNode(3)
    p4 = ListNode(4)
    p5 = ListNode(5)
    p1.pNext = p2
    p2.pNext = p3
    p3.pNext = p4
    p4.pNext = p5
    printList(p1)
    head = reverseList(p1)
    print('The reversed List is: ')
    printList(head)

def test2():
    p1 = ListNode(1)
    printList(p1)
    head = reverseList(p1)
    print('The reversed List is: ')
    printList(head)

def test3():
    p1 = None
    head = reverseList(p1)
    print('The reversed List is: ')
    printList(head)

if __name__ == '__main__':
    test1()
    test2()
    test3()