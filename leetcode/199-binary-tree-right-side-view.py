#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        def rightView(node, res, depth):
            if node is None:
                return

            if depth == len(res):
                res.append(node.val)
            rightView(node.right, res, depth + 1)
            rightView(node.left, res, depth + 1)

        if not isinstance(root, TreeNode) or root is None:
            return
        res = []
        rightView(root, res, 0)
        return res
