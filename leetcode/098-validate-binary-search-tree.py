#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, prev = [], None
        while len(stack) != 0 or root is not None:
            while root is not None:
                stack.append(root)
                root = root.left

            node = stack.pop()
            if prev is not None and prev.val >= node.val:
                return False
            prev = node
            root = node.right
        return True


