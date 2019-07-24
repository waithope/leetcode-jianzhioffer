#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def reverse(start, end):
            current = start.next
            first = current
            prev = start
            while current != end:
                nextNode = current.next
                current.next = prev
                prev = current
                current = nextNode
            start.next = prev
            first.next = current
            return first

        dummyHead = begin = ListNode(0)
        dummyHead.next = head
        count = 0
        while head is not None:
            count += 1
            nextNode = head.next
            if count % 2 == 0:
                begin = reverse(begin, nextNode)
            head = nextNode
        return dummyHead.next
