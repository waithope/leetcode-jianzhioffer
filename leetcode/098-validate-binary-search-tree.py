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
        # recursion method
        # 当前节点的所有左孩子都小于该节点的值，所有右孩子都大于该节点的值
    #     def isValid(node, lowBound, upperBound):
    #         if node is None:
    #             return True

    #         if node.val <= lowBound or node.val >= upperBound:
    #             return False

    #         left = isValid(node.left, lowBound, node.val)
    #         right = isValid(node.right, node.val, upperBound)
    #         return left and right
    #     return isValid(root, float('-inf'), float('inf'))
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


