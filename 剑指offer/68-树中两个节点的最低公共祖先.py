# -*- coding:utf-8 -*-
'''
    树中两个结点的最低公共祖先
==============================
输入两个树结点，求它们的最低公共祖先。
'''
class BinaryTreeNode(object):
    def __init__(self, val, pLeft=None, pRight=None, pParent=None):
        self.val = val
        self.pLeft = pLeft
        self.pRight = pRight
        self.pParent = pParent

def lowestCommonAncestor_BST(root, node1, node2):
    '''
    思路：当树是二叉搜索树的时候，只需简单地判断两个节点是在当前节点的哪一边，
    当两个节点的值都小于当前节点的值，则公共节点在当前节点的左边；当两个节点
    的值都大于当前节点的值，则公共节点在当前节点的右边；当一个节点在左，一个
    节点在右，则当前节点为这两个节点的公共节点。
    时间复杂度：O(n)
    '''
    if (not isinstance(root, BinaryTreeNode)
        or not isinstance(node1, BinaryTreeNode)
        or not isinstance(node1, BinaryTreeNode)):
        return None

    p1, p2 = node1, node2
    if node1.val > node2.val:
        p1, p2 = node2, node1

    node = root
    while node.val < p1.val or node.val > p2.val:
        if p2.val < node.val:
            node = node.pLeft
        if p1.val > node.val:
            node = node.pRight
    return node


def lowestCommonAncestor_HasParentPointer(root, node1, node2):
    '''
    思路：当二叉树带有父节点信息的时候，对两个节点向上回溯，并用字典记录访问过
    的节点，如果某个节点已经访问过了，就表明这个节点是这两个节点的最近公共祖先，
    直接返回该节点。
    时间复杂度O(h)
    '''
    if (not isinstance(root, BinaryTreeNode)
        or not isinstance(node1, BinaryTreeNode)
        or not isinstance(node1, BinaryTreeNode)):
        return None

    visited = {}
    p, q = node1, node2
    while p is not None or q is not None:
        if p is not None:
            if p in visited:
                return p
            visited[p] = 0
            p = p.pParent
        if q is not None:
            if q in visited:
                return q
            visited[q] = 0
            q = q.pParent
    return None


def lowestCommonAncestor_OrdinaryTree(root, node1, node2):
    '''
    思路：利用深度遍历搜索DFS分别找到从根节点到达这两个节点的路径，然后对比这两条
    路径，找到的最后一个公共节点就是这两个节点的最近公共祖先。
    时间复杂度：O(n)
    '''
    def findPath(root, node, path):
        if root is None:
            return False

        path.append(root)
        if root == node:
            return True
        left = findPath(root.pLeft, node, path)
        right = findPath(root.pRight, node, path)
        if left or right:
            return True
        path.pop()

    if (not isinstance(root, BinaryTreeNode)
        or not isinstance(node1, BinaryTreeNode)
        or not isinstance(node1, BinaryTreeNode)):
        return None

    first, second = [], []
    findPath(root, node1, first)
    findPath(root, node2, second)

    if first == [] or second == []:
        return None

    length = min(len(first), len(second))
    for i in range(1, length):
        if first[i] != second[i]:
            return first[i - 1]
    return first[-1] if len(first) < len(second) else second[-1]



'''
Test Code Here
'''
#当树为二叉搜索树时的测试用例
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

    node = lowestCommonAncestor_BST(A1, A2, A7)
    if node == A1:
        print('Test1 passed.')
    else:
        print('Test1 FAILED.')

#当树为二叉搜索树时的测试用例
#            8
#        6      10
#       5 7    9  11
def test2():
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

    node = lowestCommonAncestor_BST(A1, A4, A5)
    if node == A2:
        print('Test2 passed.')
    else:
        print('Test2 FAILED.')

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

    node = lowestCommonAncestor_BST(A1, A3, A4)
    if node == A3:
        print('Test3 passed.')
    else:
        print('Test3 FAILED.')


#当二叉树带有父节点信息时
#            8
#        6      10
#       5 7    9  11
def test4():
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
    A4.pParent, A5.pParent = A2, A2
    A6.pParent, A7.pParent = A3, A3
    A2.pParent, A3.pParent = A1, A1

    node = lowestCommonAncestor_HasParentPointer(A1, A4, A3)

    if node == A1:
        print('Test4 passed.')
    else:
        print('Test4 FAILED.')

#当树为二叉搜索树时的测试用例
#            8
#        6      10
#       5 7    9  11
def test5():
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
    A4.pParent, A5.pParent = A2, A2
    A6.pParent, A7.pParent = A3, A3
    A2.pParent, A3.pParent = A1, A1

    node = lowestCommonAncestor_HasParentPointer(A1, A6, A3)
    if node == A3:
        print('Test5 passed.')
    else:
        print('Test5 FAILED.')

#           5
#          /
#         4
#        /
#       3
#      /
#     2
#    /
#   1
def test6():
    A1 = BinaryTreeNode(5)
    A2 = BinaryTreeNode(4)
    A3 = BinaryTreeNode(3)
    A4 = BinaryTreeNode(2)
    A5 = BinaryTreeNode(1)

    A1.pLeft = A2
    A2.pLeft = A3
    A3.pLeft = A4
    A4.pLeft = A5
    A5.pParent = A4
    A4.pParent = A3
    A3.pParent = A2
    A2.pParent = A1

    node = lowestCommonAncestor_HasParentPointer(A1, A3, A4)
    if node == A3:
        print('Test6 passed.')
    else:
        print('Test6 FAILED.')


#当树为普通二叉树时
#            8
#        6      10
#       5 7    9  11
def test7():
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

    node = lowestCommonAncestor_OrdinaryTree(A1, A2, A7)
    if node == A1:
        print('Test7 passed.')
    else:
        print('Test7 FAILED.')


#           1
#          /
#         2
#        /
#       3
#      /
#     4
#    /
#   5
def test8():
    A1 = BinaryTreeNode(1)
    A2 = BinaryTreeNode(2)
    A3 = BinaryTreeNode(3)
    A4 = BinaryTreeNode(4)
    A5 = BinaryTreeNode(5)

    A1.pLeft = A2
    A2.pLeft = A3
    A3.pLeft = A4
    A4.pLeft = A5

    node = lowestCommonAncestor_OrdinaryTree(A1, A4, A5)
    if node == A4:
        print('Test8 passed.')
    else:
        print('Test8 FAILED.')

# 当要查询的节点不在树中
#           1
#          /
#         2
#        /
#       3
#      /
#     4
#    /
#   5
def test9():
    A1 = BinaryTreeNode(1)
    A2 = BinaryTreeNode(2)
    A3 = BinaryTreeNode(3)
    A4 = BinaryTreeNode(4)
    A5 = BinaryTreeNode(5)
    A6 = BinaryTreeNode(6)

    A1.pLeft = A2
    A2.pLeft = A3
    A3.pLeft = A4
    A4.pLeft = A5

    node = lowestCommonAncestor_OrdinaryTree(A1, A4, A6)
    if node == None:
        print('Test9 passed.')
    else:
        print('Test9 FAILED.')


if __name__ == '__main__':
    print('当树是二叉搜索树时的测试情况：')
    test1()
    test2()
    test3()
    print('当树带有父节点信息的测试情况：')
    test4()
    test5()
    test6()
    print('当树为普通二叉树时：')
    test7()
    test8()
    test9()