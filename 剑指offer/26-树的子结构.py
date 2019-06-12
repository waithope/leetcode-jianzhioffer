# -*- coding:utf-8 -*-
'''
    树的子结构
=================
输入两棵二叉树A和B，判断B是不是A的子结构。
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

def hasSubtree(root1, root2):
    '''
    思路：首先，需要在第一棵二叉树root1中找到与第二棵二叉树root2根节点值相同的节点，
    这个过程也是一个递归过程，当找到与root2根节点值相同的节点之后，递归地比较该节点的
    左子树是否与root2左子树相同，右子树是否与root2右子树相同，如果左右子树都相同，
    则可以知道root2是root1的子结构。
    '''
    def equal(num1, num2):
        '''
        由于计算机中存储浮点数是不精确的，所以在对浮点数进行等于判断的时候，会有一些
        意想不到的情况出现，所以调整等于的比较方式，只要num1，num2差的绝对值小于10e-8
        ，我们就认为num1==num2
        '''
        if abs(num1 - num2) < 0.00000001:
            return True
        else:
            return False

    def isSubStructure(root1, root2):
        if root2 is None:
            return True
        if root1 is None:
            return False
        if equal(root1.val, root2.val):
            return (isSubStructure(root1.pLeft, root2.pLeft)
                    and isSubStructure(root1.pRight, root2.pRight))
        return False


    result = False
    if root1 is not None and root2 is not None:
        if equal(root1.val, root2.val):
            result = isSubStructure(root1, root2)
        if not result:
            result = hasSubtree(root1.pLeft, root2)
        if not result:
            result = hasSubtree(root1.pRight, root2)
    return result


'''
Test Code Here
'''

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

    B1 = BinaryTreeNode(8)
    B2 = BinaryTreeNode(9)
    B3 = BinaryTreeNode(2)
    B1.pLeft, B1.pRight = B2, B3

    print('The Expected Value is True')
    print('The Value is: ', hasSubtree(A1, B1))

# 树中结点含有分叉，树B不是树A的子结构
#                   2                8
#               /       \           / \
#              8         3         9   2
#            /   \
#           9     5
#                / \
#               5   6
def test2():
    A1 = BinaryTreeNode(2)
    A2 = BinaryTreeNode(8)
    A3 = BinaryTreeNode(3)
    A4 = BinaryTreeNode(9)
    A5 = BinaryTreeNode(5)
    A6 = BinaryTreeNode(5)
    A7 = BinaryTreeNode(6)
    A1.pLeft, A1.pRight = A2, A3
    A2.pLeft, A2.pRight = A4, A5
    A5.pLeft, A5.pRight = A6, A7

    B1 = BinaryTreeNode(9)
    B2 = BinaryTreeNode(8)
    B3 = BinaryTreeNode(2)
    B1.pLeft, B1.pRight = B2, B3

    print('The Expected Value is False')
    print('The Value is: ', hasSubtree(A1, B1))


if __name__ == '__main__':
    test1()
    test2()