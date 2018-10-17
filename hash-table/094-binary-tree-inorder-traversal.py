'''
    Binary Tree Inorder Traversal
=====================================
Given a binary tree, return the inorder traversal of its nodes' values.

Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''


def inorderTraversal(self, root):
  """
  :type root: TreeNode
  :rtype: List[int]
  """
  # Recursive solution
  #def helper(res, node):
  #    if node:
  #        helper(res, node.left)
  #        res.append(node.val)
  #        helper(res, node.right)
  #
  #res = []
  #helper(res, root)
  #return res

  # Iterative solution
  res, stack = [], []
  while stack or root:
    if root:
      stack.append(root)
      root = root.left
    else:
      tmp = stack.pop()
      res.append(tmp.val)
      root = tmp.right
  return res


