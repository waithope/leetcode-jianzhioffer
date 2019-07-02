## Description
## Given inorder and postorder traversal of a tree, construct the binary tree.
## Note:
## You may assume that duplicates do not exist in the tree.
## For example, given
## inorder = [9,3,15,20,7]
## postorder = [9,15,7,20,3]
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

def buildTree(inorder, postorder):
  """
  :type inorder: List[int]
  :type postorder: List[int]
  :rtype: TreeNode
  """
  def helper(left, right):
    if left < right:
      node = TreeNode(postorder.pop())
      ind = index[node.val]
      node.right = helper(ind+1, right)
      node.left = helper(left, ind)
      return node
  index = {val:i for i, val in enumerate(inorder)}
  return helper(0, len(postorder))

