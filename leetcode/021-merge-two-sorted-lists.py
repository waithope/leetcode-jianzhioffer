#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # def mergeCore(node1, node2):
        #     if node1 is None:
        #         return node2
        #     if node2 is None:
        #         return node1

        #     if node1.val <= node2.val:
        #         node1.next = mergeCore(node1.next, node2)
        #         return node1
        #     else:
        #         node2.next = mergeCore(node1, node2.next)
        #         return node2

        # return mergeCore(l1, l2)
        dummyHead = ListNode(0)
        current = dummyHead
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        if l1 is None:
            current.next = l2
        else:
            current.next = l1
        return dummyHead.next

