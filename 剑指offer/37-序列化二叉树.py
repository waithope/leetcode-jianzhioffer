# -*- coding:utf-8 -*-
'''
    序列化二叉树
====================
请实现两个函数，分别用来序列化和反序列化二叉树。
序列化：将变量内容变成可存储或可传输的过程。
反序列化：将变量内容从文件中或输入流中读到内存中的过程。
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


def serilization(root):
    if root is None:
        return '$,'

    return (str(root.val) + ','
            + serilization(root.pLeft)
            + serilization(root.pRight))

def deserilization(list_of_chars):
    if not isinstance(list_of_chars, list) or len(list_of_chars) <= 0:
        return

    node = list_of_chars[0]
    if node == '$':
        node = None
    else:
        node = BinaryTreeNode(int(node))

    list_of_chars.pop(0)

    if node is not None:
        node.pLeft = deserilization(list_of_chars)
        node.pRight = deserilization(list_of_chars)

    return node


'''
Test Code Here
'''
def printTree(root):
    if root is None:
        return

    printTree(root.pLeft)
    print(root.val)
    printTree(root.pRight)

#         10
#      /      \
#     6        14
#    /         /\
#   4        12  16
def test1():
    A1 = BinaryTreeNode(10)
    A2 = BinaryTreeNode(6)
    A3 = BinaryTreeNode(14)
    A4 = BinaryTreeNode(4)
    A5 = BinaryTreeNode(12)
    A6 = BinaryTreeNode(16)

    A1.pLeft, A1.pRight = A2, A3
    A2.pLeft = A4
    A3.pLeft, A3.pRight = A5, A6

    print('The process of serilization: ')
    s = serilization(A1)
    print(s)

    print('The process of deserilization: ')
    root = deserilization(s.split(','))
    printTree(root)


if __name__ == '__main__':
    test1()

