# -*- coding:utf-8 -*-
'''
    二叉树的非递归遍历
========================
实现二叉树的非递归遍历，包括前序、中序、后续遍历
参考博客：https://blog.csdn.net/zhangxiangDavaid/article/details/37115355
'''
class BinaryTreeNode(object):
    def __init__(self, val, pLeft=None, pRight=None):
        self.val = val
        self.pLeft = pLeft
        self.pRight = pRight


def inorderWithoutRecursion(root):
    '''
    思路：中序遍历是先访问左子树再访问根节点最后访问右子树。非递归写法需要
    用到栈这种数据结构，栈有先进后出的特性。
    '''
    if not isinstance(root, BinaryTreeNode) or root is None:
        return

    stack = []
    node = root
    while len(stack) != 0 or node is not None:
        while node is not None:
            stack.append(node)
            node = node.pLeft
        if len(stack) != 0:
            node = stack.pop()
            print(node.val)
            node = node.pRight


def preorderWithoutRecursion(root):
    '''
    前序遍历，与中序遍历思路相同。
    '''
    if not isinstance(root, BinaryTreeNode) or root is None:
        return

    stack = []
    node = root
    while len(stack) != 0 or node is not None:
        while node is not None:
            print(node.val)
            stack.append(node)
            node = node.pLeft
        if len(stack) != 0:
            node = stack.pop()
            node = node.pRight


def postorderWithoutRecursion(root):
    '''
    后序遍历中根节点是在左右子节点访问后访问的，因此需要判断上次访问的节点是位于
    根节点的左子树还是右子树，如果是左子树，需要跳过根节点，进入右子树；如果是
    右子树，则直接访问根节点。
    '''
    if not isinstance(root, BinaryTreeNode) or root is None:
        return

    stack = []
    pCurrent, pLastVisited = root, None
    while pCurrent is not None:
        stack.append(pCurrent)
        pCurrent = pCurrent.pLeft
    while len(stack) != 0:
        pCurrent = stack.pop()
        if pCurrent.pRight is None or pCurrent.pRight == pLastVisited:
            print(pCurrent.val)
            pLastVisited = pCurrent
        else:
            stack.append(pCurrent)
            pCurrent = pCurrent.pRight
            while pCurrent is not None:
                stack.append(pCurrent)
                pCurrent = pCurrent.pLeft




'''
Test Code Here
'''
# 完全二叉树
#        1
#    /      \
#   2        3
#  /\       / \
# 4  5     6   7
def test1(func):
    A1 = BinaryTreeNode(1)
    A2 = BinaryTreeNode(2)
    A3 = BinaryTreeNode(3)
    A4 = BinaryTreeNode(4)
    A5 = BinaryTreeNode(5)
    A6 = BinaryTreeNode(6)
    A7 = BinaryTreeNode(7)

    A1.pLeft, A1.pRight = A2, A3
    A2.pLeft, A2.pRight = A4, A5
    A3.pLeft, A3.pRight = A6, A7

    func(A1)


# 不是完全二叉树，但是平衡二叉树
#        1
#    /      \
#   2        3
#  /\         \
# 4  5         6
#   /
#  7
def test2(func):
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

    func(A1)


# 不是平衡二叉树
#        1
#    /      \
#   2        3
#  /\
# 4  5
#   /
#  6
def test3(func):
    A1 = BinaryTreeNode(1)
    A2 = BinaryTreeNode(2)
    A3 = BinaryTreeNode(3)
    A4 = BinaryTreeNode(4)
    A5 = BinaryTreeNode(5)
    A6 = BinaryTreeNode(6)

    A1.pLeft, A1.pRight = A2, A3
    A2.pLeft, A2.pRight = A4, A5
    A5.pLeft = A6

    func(A1)

# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
def test4(func):
    A1 = BinaryTreeNode(1)
    A2 = BinaryTreeNode(2)
    A3 = BinaryTreeNode(3)
    A4 = BinaryTreeNode(4)
    A5 = BinaryTreeNode(5)

    A1.pRight = A2
    A2.pRight = A3
    A3.pRight = A4
    A4.pRight = A5

    func(A1)


if __name__ == '__main__':
    print('Test1: ')
    test1(postorderWithoutRecursion)
    print('Test2: ')
    test2(postorderWithoutRecursion)
    print('Test3: ')
    test3(postorderWithoutRecursion)
    print('Test4: ')
    test4(postorderWithoutRecursion)