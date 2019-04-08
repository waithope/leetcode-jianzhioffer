# -*- coding:utf-8 -*-
'''
    对称的二叉树
====================
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，
那么它是对称的。
二叉树节点的定义如下：
class BinaryTreeNode(object):
    def __init__(self, val, pLeft=None, pRight=None):
        self.val = val
        self.pLeft = pLeft
        self.pRight = pRight
'''

class BinaryTreeNode(object):
    def __init__(self, val, pLeft=None, pRight=None):
        self.val = val
        self.pLeft = pLeft
        self.pRight = pRight


def isSymmetrical(root):
    def isSymmetrical(root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.val != root2.val:
            return False
        return (isSymmetrical(root1.pLeft, root2.pRight)
                and isSymmetrical(root1.pRight, root2.pLeft))
    return isSymmetrical(root, root)


def printTree(root):
    if root is None:
        return

    print(root.val)
    printTree(root.pLeft)
    printTree(root.pRight)

#         9
#     7      7
#    5 3    3 5
def test1():
    A1 = BinaryTreeNode(9)
    A2 = BinaryTreeNode(7)
    A3 = BinaryTreeNode(7)
    A4 = BinaryTreeNode(5)
    A5 = BinaryTreeNode(3)
    A6 = BinaryTreeNode(3)
    A7 = BinaryTreeNode(5)
    A1.pLeft, A1.pRight = A2, A3
    A2.pLeft, A2.pRight = A4, A5
    A3.pLeft, A3.pRight = A6, A7

    print(isSymmetrical(A1))




if __name__ == '__main__':
    test1()