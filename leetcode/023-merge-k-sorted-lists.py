#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummyHead = current = ListNode(0)
        minHeap = []
        for i in range(len(lists)):
            if lists[i] is not None:
                heapq.heappush(minHeap, (lists[i].val, i, lists[i]))

        while len(minHeap) != 0:
            i, node = heapq.heappop(minHeap)[1:]
            current.next = node
            current = current.next
            if current.next is not None:
                heapq.heappush(minHeap, (current.next.val, i, current.next))
        return dummyHead.next


