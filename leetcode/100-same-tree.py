#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # if p is not None and q is not None:
        #     return (p.val == q.val
        #             and self.isSameTree(p.left, q.left)
        #             and self.isSameTree(p.right, q.right))
        # return p == q
        stack = [(p, q)]
        while stack:
            node1, node2 = stack.pop()
            if node1 is None and node2 is None:
                continue
            elif node1 is None or node2 is None:
                return False
            else:
                if node1.val != node2.val:
                    return False
                stack.append((node1.right, node2.right))
                stack.append((node1.left, node2.left))
        return True


