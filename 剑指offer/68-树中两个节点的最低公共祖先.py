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
        or not isinstance(node2, BinaryTreeNode)):
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
        or not isinstance(node2, BinaryTreeNode)):
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
    思路：利用深度优先遍历搜索DFS分别找到从根节点到达这两个节点的路径，然后
    对比这两条路径，找到的最后一个公共节点就是这两个节点的最近公共祖先。
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
        or not isinstance(node2, BinaryTreeNode)):
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


def lowestCommonAncestor_Tarjan(root, node1, node2):
    '''
    思路：tarjan算法是最近公共祖先的离线算法，可以批量查询（多次查询），但需要
    提前获取查询对，这也是这个算法的缺陷之一。该算法主要是基于并查集和深度优先搜索
    方法实现的。
    并查集：https://blog.csdn.net/liujian20150808/article/details/50848646
    Tarjan: https://blog.csdn.net/weixin_42001089/article/details/83590686
    时间复杂度O(n+q)，q为查询对的个数
    '''
    def find(x):
        if x != pre[x]:
            return find(pre[x])
        return x

    def tarjan(node, p, q):
        visited[node] = True
        if node.pLeft is not None:
            res = tarjan(node.pLeft, p, q)
            if res is not None:
                return res
            pre[node.pLeft] = node
        if node.pRight is not None:
            res = tarjan(node.pRight, p, q)
            if res is not None:
                return res
            pre[node.pRight] = node
        if node == p and visited[q]:
            return find(q)
        if node == q and visited[p]:
            return find(p)

    def depthFirstSearch(node):
        if node is not None:
            pre[node] = node
            visited[node] = False
            depthFirstSearch(node.pLeft)
            depthFirstSearch(node.pRight)

    if (not isinstance(root, BinaryTreeNode)
        or not isinstance(node1, BinaryTreeNode)
        or not isinstance(node2, BinaryTreeNode)):
        return None

    visited, pre = {}, {}
    depthFirstSearch(root)
    if node1 not in visited or node2 not in visited:
        return None
    return tarjan(root, node1, node2)

import math
def lowestCommonAncestor_RMQ(root, node1, node2):
    '''
    思路：最近公共祖先问题可以转化为RMQ区间最值查询问题，RMQ是一种先进行
    O(nlogn)预处理，然后O(1)在线查询的算法。所谓区间最值查询，是指在一个
    数组中查找两个指定索引中最小值的位置。先通过DFS获取树的欧拉序列以及对应
    的深度序列(每个节点在树中的深度)，然后构建Sparse Table，这个表就是用于
    解决给定区间求最值的问题，一旦构建完成后，查询的时间为O(1)。
    RMQ：https://blog.csdn.net/weixin_42001089/article/details/83590686
    欧拉序列：https://www.cnblogs.com/pealicx/p/6859901.html
    树的欧拉序列是对树进行深度优先遍历DFS的一种序列。有两种形式：1、在
    每个节点进和出都加进序列，最终每个节点恰好出现两次。2、在遍历的时候只要到达一个
    节点就加进序列。
    '''
    def depthFirstSearch(root, d):
        depths.append(d)
        eulers.append(root)
        if root not in first.keys():
            first[root] = len(eulers)
        if root.pLeft is not None:
            depthFirstSearch(root.pLeft, d + 1)
            eulers.append(root)
            depths.append(d)
        if root.pRight is not None:
            depthFirstSearch(root.pRight, d + 1)
            eulers.append(root)
            depths.append(d)

    def buildSparseTable(length):
        k = int(math.log(length, 2))
        for i in range(length):
            st[i + 1] = [i + 1]
        for j in range(1, k + 1):
            i = 1
            pos = i + 2 ** j - 1
            while pos <= length:
                a = st[i][j - 1]
                b = st[i + 2 ** (j - 1)][j - 1]
                if depths[a - 1] <= depths[b - 1]:
                    st[i].append(a)
                else:
                    st[i].append(b)
                i += 1
                pos += 1

    def RMQ(m, n):
        k = int(math.log(n - m + 1, 2))
        a = st[m][k]
        b = st[n - 2 ** k + 1][k]
        if depths[a - 1] <= depths[b - 1]:
            return a
        else:
            return b

    def LCA(node1, node2):
        if first[node1] < first[node2]:
            res = RMQ(first[node1], first[node2])
        else:
            res = RMQ(first[node2], first[node1])
        return eulers[res - 1]


    if (not isinstance(root, BinaryTreeNode)
        or not isinstance(node1, BinaryTreeNode)
        or not isinstance(node2, BinaryTreeNode)):
        return None

    # eulers代表欧拉序列， depths记录序列每个节点的深度
    eulers, depths = [], []

    # first记录每一个元素在欧拉序列中首次出现的位置
    first = {}

    # st记录每段区间最值，它的结构是这样{1: [1, 1, 1], 2: [2, 2, 11], ...}
    # 比如2: [2, 2, 11]代表的意义就是从第二个位置开始，长度为1的区间中(本身)
    # 深度最浅元素的位置是2，长度为2的区间中深度最浅元素的位置是2；长度为4的区间中
    # (本身)深度最浅元素的位置是11
    st = {}
    depthFirstSearch(root, 1)
    if node1 not in first or node2 not in first:
        return None
    buildSparseTable(len(depths))
    return LCA(node1, node2)


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


#最近公共祖先的tarjan离线算法测试用例
#            8
#        6      10
#       5 7    9  11
def test10():
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

    node = lowestCommonAncestor_Tarjan(A1, A2, A7)
    if node == A1:
        print('Test10 passed.')
    else:
        print('Test10 FAILED.')


#           1
#          /
#         2
#        /
#       3
#      /
#     4
#    /
#   5
def test11():
    A1 = BinaryTreeNode(1)
    A2 = BinaryTreeNode(2)
    A3 = BinaryTreeNode(3)
    A4 = BinaryTreeNode(4)
    A5 = BinaryTreeNode(5)

    A1.pLeft = A2
    A2.pLeft = A3
    A3.pLeft = A4
    A4.pLeft = A5

    node = lowestCommonAncestor_Tarjan(A1, A4, A5)
    if node == A4:
        print('Test11 passed.')
    else:
        print('Test11 FAILED.')

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
def test12():
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

    node = lowestCommonAncestor_Tarjan(A1, A4, A6)
    if node == None:
        print('Test12 passed.')
    else:
        print('Test12 FAILED.')


#最近公共祖先的RMQ在线算法测试用例
#            8
#        6      10
#       5 7    9  11
def test13():
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

    node = lowestCommonAncestor_RMQ(A1, A2, A7)
    if node == A1:
        print('Test13 passed.')
    else:
        print('Test13 FAILED.')


#           1
#          /
#         2
#        /
#       3
#      /
#     4
#    /
#   5
def test14():
    A1 = BinaryTreeNode(1)
    A2 = BinaryTreeNode(2)
    A3 = BinaryTreeNode(3)
    A4 = BinaryTreeNode(4)
    A5 = BinaryTreeNode(5)

    A1.pLeft = A2
    A2.pLeft = A3
    A3.pLeft = A4
    A4.pLeft = A5

    node = lowestCommonAncestor_RMQ(A1, A4, A5)
    if node == A4:
        print('Test14 passed.')
    else:
        print('Test14 FAILED.')

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
def test15():
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

    node = lowestCommonAncestor_RMQ(A1, A4, A6)
    if node == None:
        print('Test15 passed.')
    else:
        print('Test15 FAILED.')


if __name__ == '__main__':
    print('当树是二叉搜索树时的测试情况：')
    test1()
    test2()
    test3()
    print('当树带有父节点信息时的测试情况：')
    test4()
    test5()
    test6()
    print('当树为普通二叉树时的测试情况：')
    test7()
    test8()
    test9()
    print('Tarjan离线算法测试情况：')
    test10()
    test11()
    test12()
    print('RMQ在线算法测试情况：')
    test13()
    test14()
    test15()