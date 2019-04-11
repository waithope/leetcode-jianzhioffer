# -*- coding:utf-8 -*-
'''
    分行从上到下打印二叉树
===========================
从上到下打印二叉树，同一层的节点按照从左到右的顺序打印。每一层打印到一行。
例如，输入下图的二叉树:
#         8
#     6      10
#   5   7  9    11
输出：
8
6 10
5 7 9 11

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


import queue
def printTreeHierarchical(root):
    '''
    思路：在从上到下打印二叉树题目的基础上，用两个变量分别记录当前层未打印的
    节点数和下一层的节点数目。
    '''
    if root is None:
        return

    queueTree = queue.Queue()
    queueTree.put(root)
    currentLevel = 1
    nextLevel = 0
    while not queueTree.empty():
        node = queueTree.get()
        print(node.val, end=' ')
        currentLevel -= 1

        if node.pLeft is not None:
            queueTree.put(node.pLeft)
            nextLevel += 1
        if node.pRight is not None:
            queueTree.put(node.pRight)
            nextLevel += 1

        if currentLevel == 0:
            print('\r')
            currentLevel = nextLevel
            nextLevel = 0


#         9
#     6      7
#    5 4    3 2
def test1():
    A1 = BinaryTreeNode(9)
    A2 = BinaryTreeNode(6)
    A3 = BinaryTreeNode(7)
    A4 = BinaryTreeNode(5)
    A5 = BinaryTreeNode(4)
    A6 = BinaryTreeNode(3)
    A7 = BinaryTreeNode(2)
    A1.pLeft, A1.pRight = A2, A3
    A2.pLeft, A2.pRight = A4, A5
    A3.pLeft, A3.pRight = A6, A7

    printTreeHierarchical(A1)


#               5
#              /
#             4
#            /
#           3
#          /
#         2
#        /
#       1
def test2():
    A1 = BinaryTreeNode(5)
    A2 = BinaryTreeNode(4)
    A3 = BinaryTreeNode(3)
    A4 = BinaryTreeNode(2)
    A5 = BinaryTreeNode(1)
    A1.pLeft = A2
    A2.pLeft = A3
    A3.pLeft = A4
    A4.pLeft = A5

    printTreeHierarchical(A1)

#     5
#       \
#         4
#           \
#            3
#              \
#               2
#                 \
#                  1
def test3():
    A1 = BinaryTreeNode(5)
    A2 = BinaryTreeNode(4)
    A3 = BinaryTreeNode(3)
    A4 = BinaryTreeNode(2)
    A5 = BinaryTreeNode(1)
    A1.pRight = A2
    A2.pRight = A3
    A3.pRight = A4
    A4.pRight = A5

    printTreeHierarchical(A1)


if __name__ == '__main__':
    test1()
    test2()
    test3()