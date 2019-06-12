# -*- coding:utf-8 -*-
'''
    二叉树的镜像
====================
请完成一个函数，输入一棵二叉树，该函数输出它的镜像。
二叉树节点的定义如下：
class BinaryTreeNode(object):
    def __init__(self, val, pLeft=None, pRight=None):
        self.val = val
        self.pLeft = pLeft
        self.pRight = pRight

                   8
               /       \
              6         10
            /   \     /    \
           5     7   9      11

                   8
               /       \
              10        6
            /   \     /    \
           11    9   7      5
'''

class BinaryTreeNode(object):
    def __init__(self, val, pLeft=None, pRight=None):
        self.val = val
        self.pLeft = pLeft
        self.pRight = pRight

def mirror(root):
    '''
    思路：镜像其实就是左右对称，通过画图观察，通过对每个节点的左右两个子节点进行
    递归地交换，直到节点没有子节点（0个子节点）停止，最终得到的就是镜像二叉树。
    '''
    if root is None:
        return
    if root.pLeft is None and root.pRight is None:
        return

    temp = root.pLeft
    root.pLeft = root.pRight
    root.pRight = temp

    if root.pLeft:
        mirror(root.pLeft)
    if root.pRight:
        mirror(root.pRight)


'''
Test Code Here
'''
def printTree(root):
    if root is None:
        return

    print(root.val)
    printTree(root.pLeft)
    printTree(root.pRight)

# 树中结点含有分叉，树B是树A的子结构
#                   2                8
#               /       \           / \
#              8         3         9   2
#            /   \
#           9     2
#                / \
#               5   6
def test1():
    A1 = BinaryTreeNode(2)
    A2 = BinaryTreeNode(8)
    A3 = BinaryTreeNode(3)
    A4 = BinaryTreeNode(9)
    A5 = BinaryTreeNode(2)
    A6 = BinaryTreeNode(5)
    A7 = BinaryTreeNode(6)
    A1.pLeft, A1.pRight = A2, A3
    A2.pLeft, A2.pRight = A4, A5
    A5.pLeft, A5.pRight = A6, A7

    printTree(A1)
    print('Mirror Once: ')
    mirror(A1)
    printTree(A1)
    print('Mirror Another Time: ')
    mirror(A1)
    printTree(A1)


if __name__ == '__main__':
    test1()