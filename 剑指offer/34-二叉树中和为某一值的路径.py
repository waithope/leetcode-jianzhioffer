# -*- coding:utf-8 -*-
'''
    二叉树中和为某一值的路径
=============================
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的
根节点开始往下一直到**叶节点**所经过的节点形成一条路径。
例如，输入下图的二叉树和整数22:
#         10
#     5      12
#   4   7
则打印出两条路径，第一条路径包含节点10、12，第二条路径包含节点10、5和7。
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


def findPath(root, target):
    '''
    思路：由题意可以看出，在计算路径和的过程中，需要首先访问根节点，因此这里
    我们需要进行前序遍历，每遍历一个节点，就累加当前节点的值，并判断累加和
    是否等于target以及当前节点是否为叶子节点，如果同时满足，打印路径；否则
    继续遍历，直到整棵树遍历完为止。
    注：在从子结点返回到父节点前，需要将当前路径集合中的最后一个节点删去，
    并从累加和中减去子结点的值。
    '''
    def findPath(node, target, path, current):
        path.append(node)
        current += node.val

        isLeaf = False
        if node.pLeft is None and node.pRight is None:
            isLeaf = True

        if isLeaf and current == target:
            print('The path is Found')
            for t in path:
                print(t.val, end=' ')
            print('\n')

        if node.pLeft is not None:
            findPath(node.pLeft, target, path, current)
        if node.pRight is not None:
            findPath(node.pRight, target, path, current)

        current -= node.val
        path.pop()

    if root is None:
        return

    path, current = [], 0
    findPath(root, target, path, current)


'''
Test Code Here
'''
#         10
#     5      12
#   4  7
def test1():
    A1 = BinaryTreeNode(10)
    A2 = BinaryTreeNode(5)
    A3 = BinaryTreeNode(12)
    A4 = BinaryTreeNode(4)
    A5 = BinaryTreeNode(7)

    A1.pLeft, A1.pRight = A2, A3
    A2.pLeft, A2.pRight = A4, A5

    print('Two paths should be found in Test1.')
    findPath(A1, 22)


#         10
#     5      12
#   4  7
def test2():
    A1 = BinaryTreeNode(10)
    A2 = BinaryTreeNode(5)
    A3 = BinaryTreeNode(12)
    A4 = BinaryTreeNode(4)
    A5 = BinaryTreeNode(7)

    A1.pLeft, A1.pRight = A2, A3
    A2.pLeft, A2.pRight = A4, A5

    print('No paths should be found in Test2.')
    findPath(A1, 15)


#           5
#          /
#         4
#        /
#       3
#      /
#     2
#    /
#   1
def test3():
    A1 = BinaryTreeNode(5)
    A2 = BinaryTreeNode(4)
    A3 = BinaryTreeNode(3)
    A4 = BinaryTreeNode(2)
    A5 = BinaryTreeNode(1)

    A1.pLeft = A2
    A2.pLeft = A3
    A3.pLeft = A4
    A4.pLeft = A5

    print('One path should be found in Test3.')
    findPath(A1, 15)


# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
def test4():
    A1 = BinaryTreeNode(5)
    A2 = BinaryTreeNode(4)
    A3 = BinaryTreeNode(3)
    A4 = BinaryTreeNode(2)
    A5 = BinaryTreeNode(1)

    A1.pRight = A2
    A2.pRight = A3
    A3.pRight = A4
    A4.pRight = A5

    print('No path should be found in Test4.')
    findPath(A1, 16)


def test5():
    A1 = BinaryTreeNode(1)

    print('One path should be found in Test5.')
    findPath(A1, 1)

def test6():
    A1 = None
    print('No path should be found in Test6.')
    findPath(A1, 0)


if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
