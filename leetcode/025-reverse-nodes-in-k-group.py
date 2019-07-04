'''
    Reverse Nodes in k-Group
================================
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
'''
#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(start, end):
            currentNode = start.next
            firstNode = currentNode
            nextNode = None
            prevNode = start
            while currentNode != end:
                nextNode = currentNode.next
                currentNode.next = prevNode
                prevNode = currentNode
                currentNode = nextNode
            start.next = prevNode
            firstNode.next = currentNode
            return firstNode

        if not isinstance(head, ListNode):
            return
        if head is None  or not isinstance(k, int) or k <= 1:
            return head

        # 哑变量，记录表头的位置，从程序运行完毕，该变量始终指向表头
        dummyHead = ListNode(-1)
        dummyHead.next = head
        begin = dummyHead
        count = 0
        while head is not None:
            count += 1
            nextNode = head.next
            if count % k == 0:
                begin = reverse(begin, head.next)
            head = nextNode
        return dummyHead.next

