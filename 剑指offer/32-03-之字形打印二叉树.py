# -*- coding:utf-8 -*-
'''
    之字形打印二叉树
=======================
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层
按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
例如，输入下图的二叉树:
#         8
#     6      10
#   5   7  9    11
输出：
8
10 6
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


def printTreeZigZagShape(root):
    if root is None:
        return

    stackTree = [[] for i in range(2)]
    current, nxt = 1, 0
    stackTree[current].append(root)
    while stackTree[current] != [] or stackTree[nxt] != []:
        if current:
            node = stackTree[current].pop()
            print(node.val, end=' ')
            if node.pLeft is not None:
                stackTree[nxt].append(node.pLeft)
            if node.pRight is not None:
                stackTree[nxt].append(node.pRight)
        else:
            node = stackTree[current].pop()
            print(node.val, end=' ')
            if node.pRight is not None:
                stackTree[nxt].append(node.pRight)
            if node.pLeft is not None:
                stackTree[nxt].append(node.pLeft)

        if stackTree[current] == []:
            print('\r')
            nxt = current
            current = 1 - current


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

    print('Test1: ')
    printTreeZigZagShape(A1)


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

    print('Test2: ')
    printTreeZigZagShape(A1)

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

    print('Test3: ')
    printTreeZigZagShape(A1)


if __name__ == '__main__':
    test1()
    test2()
    test3()
