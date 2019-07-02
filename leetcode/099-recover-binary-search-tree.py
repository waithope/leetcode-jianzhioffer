#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev, stack, first, second = None, [], None, None
        while len(stack) != 0 or root is not None:
            while root is not None:
                stack.append(root)
                root = root.left
            if not stack:
                break
            node = stack.pop()
            if prev is not None and prev.val > node.val:
                if first is None:
                    first = prev
                second = node
            prev = node
            root = node.right
        first.val, second.val = second.val, first.val



