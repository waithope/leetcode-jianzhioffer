#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return

        stack = []
        stack.append(root)
        while len(stack) != 0:
            node = stack.pop()
            if node is None:
                continue
            left = node.left
            right = node.right
            node.left, node.right = right, left
            stack.append(left)
            stack.append(right)
        return root


