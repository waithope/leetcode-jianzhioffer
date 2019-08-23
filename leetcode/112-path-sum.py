#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def pathSum(root, sum):
            if not root:
                return False

            if (root.left is None and root.right is None
                and root.val == sum):
                return True

            sum -= root.val
            return (pathSum(root.left, sum)
                    or pathSum(root.right, sum))
        return pathSum(root, sum)


