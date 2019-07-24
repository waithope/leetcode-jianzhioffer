#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # def isSymmetric(node1, node2):
        #     if node1 is None and node2 is None:
        #         return True
        #     elif node1 is None or node2 is None:
        #         return False
        #     elif node1.val != node2.val:
        #         return False

        #     return (isSymmetric(node1.left, node2.right)
        #             and isSymmetric(node1.right, node2.left))
        # return isSymmetric(root, root)
        if root is None:
            return True

        stack = []
        stack.append(root.left)
        stack.append(root.right)
        while len(stack) != 0:
            node1, node2 = stack.pop(), stack.pop()
            if node1 is None and node2 is None:
                continue
            elif node1 is None or node2 is None:
                return False
            elif node1.val != node2.val:
                return False
            stack.append(node1.left)
            stack.append(node2.right)
            stack.append(node1.right)
            stack.append(node2.left)
        return True


