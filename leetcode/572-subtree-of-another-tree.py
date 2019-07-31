#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def equal(num1, num2):
            if abs(num1 - num2) < 0.00000001:
                return True
            else:
                return False
        def isMatch(root1, root2):
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None:
                return False
            else:
                return (equal(root1.val, root2.val)
                        and isMatch(root1.left, root2.left)
                        and isMatch(root1.right, root2.right))
        def hasSubtree(s, t):
            result = False
            if s is not None and t is not None:
                if equal(s.val, t.val):
                    result = isMatch(s, t)
                if not result:
                    result = hasSubtree(s.left, t)
                if not result:
                    result = hasSubtree(s.right, t)
            return result
        return hasSubtree(s, t)

