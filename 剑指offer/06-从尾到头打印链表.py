# -*- coding:utf-8 -*-
'''
    从尾到头打印链表
=======================
输入一个链表的头节点，从尾到头反过来打印出每个节点的值。
'''

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def printListFromTailtoHead1(head):
    '''
    从头遍历链表，遍历过程中将val压入栈中
    时间：O(n)
    '''
    if head is None:
        return

    stack = []
    node = head
    while node is not None:
        stack.append(node.val)
        node = node.next
    while len(stack):
        print(stack.pop())

def printListFromTailtoHead2(head):
    '''
    用递归方式实现，当链表非常长时，会导致函数调用栈溢出
    '''
    if head is None:
        return

    printListFromTailtoHead2(head.next)
    print(head.val)


if __name__ == '__main__':
    n1 = ListNode(3)
    n2 = ListNode(0)
    n3 = ListNode(-1)
    n1.next = n2
    n2.next = n3
    printListFromTailtoHead1(n1)
    printListFromTailtoHead2(n1)


