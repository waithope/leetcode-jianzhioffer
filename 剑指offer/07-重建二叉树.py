# -*- coding:utf-8 -*-
'''
        重建二叉树
=========================
输入某二叉树的前序遍历和中序遍历结果，请重建改二叉树。
假如输入的前序遍历和中序遍历的结果中都不含重复的数字。例如，输入前序遍历序列
{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并输出
它的头节点。
'''

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def reConstructBinaryTree(preorder, inorder):
    # 检查输入序列的有效性
    if not isinstance(preorder, list) \
        or not isinstance(inorder, list) \
        or len(preorder) != len(inorder):
        return

    root = createTreeRecursively(preorder, inorder)
    return root

def createTreeRecursively(preorder, inorder):
    if len(preorder) == 0:
        return None

    root = TreeNode(preorder[0])
    index = inorder.index(root.val)
    root.left = createTreeRecursively(preorder[1:index+1], inorder[:index])
    root.right = createTreeRecursively(preorder[index+1:], inorder[index+1:])
    return root

def print_level(node, position_name):
    if node is None:
        return
    print(position_name, " ", node.val)
    print_level(node.left, "left")
    print_level(node.right, "right")

if __name__ == '__main__':
    preorder = [1,2,4,7,3,5,6,8]
    inorder = [4,7,2,1,5,3,8,6]
    head = reConstructBinaryTree(preorder, inorder)
    print_level(head, 'root')


