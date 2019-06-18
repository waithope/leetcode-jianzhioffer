# -*- coding:utf-8 -*-
'''
        二叉树的深度
============================
输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、
叶节点）形成树的一条路径，最长路径的长度为树的深度。
'''

class BinaryTreeNode(object):
    def __init__(self, val, pLeft=None, pRight=None):
        self.val = val
        self.pLeft = pLeft
        self.pRight = pRight


def treeDepth(pRoot):
    '''
    思路：根据定义，整棵树的深度就是树当中的最长路径，其实就是根节点左右子树深度
    的较大者加上1，因此，利用递归的方法就可以简便的得到树的深度。
    '''
    def treeDepthCore(root):
        if root is None:
            return 0

        left = treeDepthCore(root.pLeft)
        right = treeDepthCore(root.pRight)
        return max(left, right) + 1

    if not isinstance(pRoot, BinaryTreeNode) or pRoot is None:
        return 0

    return treeDepthCore(pRoot)


'''
Test Code Here
'''
#        1
#     /      \
#    2        3
#   /\         \
#  4  5         6
#    /
#   7
def test1():
    A1 = BinaryTreeNode(1)
    A2 = BinaryTreeNode(2)
    A3 = BinaryTreeNode(3)
    A4 = BinaryTreeNode(4)
    A5 = BinaryTreeNode(5)
    A6 = BinaryTreeNode(6)
    A7 = BinaryTreeNode(7)

    A1.pLeft, A1.pRight = A2, A3
    A2.pLeft, A2.pRight = A4, A5
    A3.pRight = A6
    A5.pLeft = A7

    depth = treeDepth(A1)
    if depth == 4:
        print('Test1 Passed.')
    else:
        print('Test1 FAILED.')


# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
def test2():
    A1 = BinaryTreeNode(1)
    A2 = BinaryTreeNode(2)
    A3 = BinaryTreeNode(3)
    A4 = BinaryTreeNode(4)
    A5 = BinaryTreeNode(5)

    A1.pRight = A2
    A2.pRight = A3
    A3.pRight = A4
    A4.pRight = A5

    depth = treeDepth(A1)
    if depth == 5:
        print('Test2 Passed.')
    else:
        print('Test2 FAILED.')


# 树中只有1个结点
def test3():
    A1 = BinaryTreeNode(1)

    depth = treeDepth(A1)
    if depth == 1:
        print('Test3 Passed.')
    else:
        print('Test3 FAILED.')


if __name__ == '__main__':
    test1()
    test2()
    test3()