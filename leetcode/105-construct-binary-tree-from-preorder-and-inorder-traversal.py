## Description
## Given preorder and inorder traversal of a tree, construct the binary tree.
## Note:
## You may assume that duplicates do not exist in the tree.
## preorder = [3,9,20,15,7]
## inorder = [9,3,15,20,7]
## Return the following binary tree:
##     3
##    / \
##   9  20
##     /  \
##    15   7

# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

def buildTree(preorder, inorder):
  """
  :type preorder: List[int]
  :type inorder: List[int]
  :rtype: TreeNode
  """
  def helper(left, right):
    if left < right:
      node = TreeNode(preorder.pop())
      ind = index[node.val]       # ind splits the tree to left subtree and right subtree
      node.left = helper(left, ind)
      node.right = helper(ind+1, right)
      return node

  index = {val:i for i, val in enumerate(inorder)}
  preorder.reverse()
  return helper(0, len(preorder))

