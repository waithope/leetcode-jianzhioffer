# -*- coding:utf-8 -*-
'''
    二叉搜索树的第k小节点
============================
给定一棵二叉搜索树，请找出其中的第k小的节点。例如，在下图的二叉搜索树里，
按节点数值大小顺序，第三小的节点值是4。
     5
 3       7
2 4    6   8
'''

class BinaryTreeNode(object):
    def __init__(self, val, pLeft=None, pRight=None):
        self.val = val
        self.pLeft = pLeft
        self.pRight = pRight

def findKthNode(pRoot, k):
    '''
    思路：二叉搜索树的中序遍历序列是按节点数值大小顺序排序的，因此，只要按照
    中序遍历算法就能很容易的找到第k小的节点。
    '''
    def findKthNodeCore(root, k):
        if root is None:
            return None

        node = findKthNodeCore(root.pLeft, k)
        if node is not None:
            return node
        global index
        index += 1
        if k == index:
            return root
        node = findKthNodeCore(root.pRight, k)
        if node is not None:
            return node

    if (not isinstance(pRoot, BinaryTreeNode) or pRoot is None
        or not isinstance(k, int) or k == 0):
        return None
    global index
    index = 0
    return findKthNodeCore(pRoot, k)


def findKthNode_Iteratively(root, k):
    if (not isinstance(root, BinaryTreeNode) or root is None
        or not isinstance(k, int) or k <= 0):
        return

    stack = []
    node = root
    while len(stack) != 0 or node is not None:
        while node is not None:
            stack.append(node)
            node = node.pLeft
        if len(stack) != 0:
            node = stack.pop()
            k -= 1
            if k == 0:
                return node
            node = node.pRight
    return None


'''
Test Code Here
'''
def printTree(root):
    if root is None:
        return

    printTree(root.pLeft)
    print(root.val)
    printTree(root.pRight)

def test(pRoot, k, expected):
    node = findKthNode_Iteratively(pRoot, k)
    if node is None:
        print(None)
    elif node.val == expected:
        print('Passed.')
    else:
        print('FAILED.')

#            8
#        6      10
#       5 7    9  11
def test1():
    A1 = BinaryTreeNode(8)
    A2 = BinaryTreeNode(6)
    A3 = BinaryTreeNode(10)
    A4 = BinaryTreeNode(5)
    A5 = BinaryTreeNode(7)
    A6 = BinaryTreeNode(9)
    A7 = BinaryTreeNode(11)

    A1.pLeft, A1.pRight = A2, A3
    A2.pLeft, A2.pRight = A4, A5
    A3.pLeft, A3.pRight = A6, A7

    test(A1, 0, None)
    test(A1, 1, 5)
    test(A1, 2, 6)
    test(A1, 3, 7)
    test(A1, 4, 8)
    test(A1, 5, 9)
    test(A1, 6, 10)
    test(A1, 7, 11)
    test(A1, 8, None)

#           5
#          /
#         4
#        /
#       3
#      /
#     2
#    /
#   1
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

    test(A1, 0, None)
    test(A1, 1, 1)
    test(A1, 2, 2)
    test(A1, 3, 3)
    test(A1, 4, 4)
    test(A1, 5, 5)
    test(A1, 6, None)

if __name__ == '__main__':
    test1()
    test2()
