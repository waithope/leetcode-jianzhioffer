# -*- coding:utf-8 -*-
'''
    圆圈中最后剩下的数字
==========================
0，1, …，n-1这n个数字排成一个圆圈，从数字0开始每次从这个圆圈里删除第m个数字。
求出这个圆圈里剩下的最后一个数字。例如，0、1、2、3、4这5个数字组成一个圆圈，从
数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下3。
'''

class LinkedList(object):
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt


def lastRemaining_linkedList(n, m):
    '''
    思路：经典的解法是通过一个循环链表进行存储这n个数字，然后通过遍历依次删除
    对应位置的节点。
    时间效率为O(nm)
    '''
    if (not isinstance(n, int) or n < 0
        or not isinstance(m, int) or m <=0):
        return -1

    head = LinkedList(0)
    pre = head
    i = 1
    while i < n:
        node = LinkedList(i)
        pre.next = node
        pre = node
        i += 1
    pre.next = head

    node = head
    while node.val != node.next.val:
        for _ in range(m - 1):
            pre = node
            node = node.next
        pre.next = node.next
        node = pre.next
    return node.val


import unittest

class TestLastRemaining(unittest.TestCase):
    def test_last_remaining(self):
        self.assertEqual(lastRemaining_linkedList(5,3), 3)
        self.assertEqual(lastRemaining_linkedList(5,2), 2)
        self.assertEqual(lastRemaining_linkedList(6,7), 4)
        self.assertEqual(lastRemaining_linkedList(6,6), 3)
        self.assertEqual(lastRemaining_linkedList(0,0), -1)
        self.assertEqual(lastRemaining_linkedList(4000,997), 1027)


if __name__ == '__main__':
    unittest.main()



