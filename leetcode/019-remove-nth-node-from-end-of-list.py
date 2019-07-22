#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if (not isinstance(head, ListNode) or not isinstance(n, int)
            or n < 1):
            return head

        listLen = 0
        node = head
        while node is not None:
            listLen += 1
            node = node.next
        if n > listLen:
            return head
        elif n == listLen:
            return head.next
        else:
            prevNode, node = None, head
            for i in range(listLen - n):
                prevNode = node
                node = node.next
            prevNode.next = node.next
            return head

