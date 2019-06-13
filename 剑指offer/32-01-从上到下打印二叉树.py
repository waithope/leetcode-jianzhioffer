# -*- coding:utf-8 -*-
'''
    从上到下打印二叉树
========================
从上到下打印二叉树的每个节点，同一层的节点按照从左到右的顺序打印。例如，输入
下图的二叉树，则依次打印出8,6,10,5,7,9,11。
#         8
#     6      10
#   5   7  9    11
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
def printTreeTopToBottom(root):
    '''
    思路：题目要求从第1层到第k层，且每一层从左到右打印节点的值，解题方法是
    利用队列数据结构，首先将根节点push到队列中，接着pop一个节点，打印其
    值，并将该节点的左右子节点push到队列中(如果有子节点的话)，先push左子节点
    再push右子节点，由于队列是先入先出结构，这样就保证了每一层能够从左到右打印
    节点的值。重复上述步骤直至最后队列为空。
    '''
    if root is None:
        return

    queueTree = queue.Queue()
    queueTree.put(root)
    res = []
    while not queueTree.empty():
        node = queueTree.get()
        res.append(node.val)
        if node.pLeft is not None:
            queueTree.put(node.pLeft)
        if node.pRight is not None:
            queueTree.put(node.pRight)
    return res


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

    assert(printTreeTopToBottom(A1)==[9,6,7,5,4,3,2])

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

    assert(printTreeTopToBottom(A1)==[5,4,3,2,1])


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

    assert(printTreeTopToBottom(A1)==[5,4,3,2,1])


if __name__ == '__main__':
    test1()
    test2()
    test3()
