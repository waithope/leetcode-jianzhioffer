# -*- coding:utf-8 -*-
'''
        平衡二叉树
============================
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树
的深度相差不超过1，那么它就是一棵平衡二叉树。
'''
class BinaryTreeNode(object):
    def __init__(self, val, pLeft=None, pRight=None):
        self.val = val
        self.pLeft = pLeft
        self.pRight = pRight

def isBalanced(pRoot):
    def isBalancedCore(root):
        if root is None:
            return True, 0

        isLeftBalanced, leftDepth = isBalancedCore(root.pLeft)
        isRightBalanced, rightDepth = isBalancedCore(root.pRight)

        if (isLeftBalanced and isRightBalanced
            and abs(leftDepth - rightDepth) <= 1):
            depth = max(leftDepth, rightDepth) + 1
            return True, depth

        return False, None

    if not isinstance(pRoot, BinaryTreeNode) or pRoot is None:
        return True

    return isBalancedCore(pRoot)


'''
Test Code Here
'''
# 完全二叉树
#        1
#    /      \
#   2        3
#  /\       / \
# 4  5     6   7
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
    A3.pLeft, A3.pRight = A6, A7

    res, _ = isBalanced(A1)
    if res:
        print('Test1 Passed.')
    else:
        print('Test1 FAILED.')


# 不是完全二叉树，但是平衡二叉树
#        1
#    /      \
#   2        3
#  /\         \
# 4  5         6
#   /
#  7
def test2():
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

    res, _ = isBalanced(A1)
    if res:
        print('Test2 Passed.')
    else:
        print('Test2 FAILED.')


# 不是平衡二叉树
#        1
#    /      \
#   2        3
#  /\
# 4  5
#   /
#  6
def test3():
    A1 = BinaryTreeNode(1)
    A2 = BinaryTreeNode(2)
    A3 = BinaryTreeNode(3)
    A4 = BinaryTreeNode(4)
    A5 = BinaryTreeNode(5)
    A6 = BinaryTreeNode(6)

    A1.pLeft, A1.pRight = A2, A3
    A2.pLeft, A2.pRight = A4, A5
    A5.pLeft = A6

    res, _ = isBalanced(A1)
    if not res:
        print('Test3 Passed.')
    else:
        print('Test3 FAILED.')


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
    A1 = BinaryTreeNode(1)
    A2 = BinaryTreeNode(2)
    A3 = BinaryTreeNode(3)
    A4 = BinaryTreeNode(4)
    A5 = BinaryTreeNode(5)

    A1.pRight = A2
    A2.pRight = A3
    A3.pRight = A4
    A4.pRight = A5

    res, _ = isBalanced(A1)
    if not res:
        print('Test4 Passed.')
    else:
        print('Test4 FAILED.')


def test5():
    A1 = BinaryTreeNode(1)

    res, _ = isBalanced(A1)
    if res:
        print('Test5 Passed.')
    else:
        print('Test5 FAILED.')


if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()