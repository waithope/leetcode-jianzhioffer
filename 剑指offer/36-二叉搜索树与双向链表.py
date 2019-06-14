# -*- coding:utf-8 -*-
'''
    二叉搜索树与双向链表
=========================
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何节点，
只能调整树中节点指针的指向。
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


def convert(root):
    '''
    思路：排序的双向链表，链表中的每个节点有两个指针，一个指针指向
    前一个节点，一个指针指向后一个节点。而二叉搜索树的每一个节点也
    有两个指针，一个指向左子树，一个指向右子树。利用这种相同的结构
    实现树到双向链表的转换。原先指向左子节点的指针调整为链表中指向
    前一个节点的指针，原先指向右子结点的指针调整为指向后一个节点的
    指针。由于二叉搜索树的中序遍历就是按照从小到大的顺序进行访问，
    所以在访问的过程中，需要保存上一个节点的指针。假设访问到根节点
    的时候，将根节点的pLeft设置为上一个节点，如果上一个节点不为空，
    则把上一个节点的pRight设置为当前的根节点，这样一来，上一个节点
    和当前节点的双向就建立好了，一直递归下去，最后返回双向链表的尾节点，
    通过向前遍历到头节点，返回头节点。
    '''
    def convertNode(node, pLastNode):
        if node is None:
            return

        if node.pLeft is not None:
            pLastNode = convertNode(node.pLeft, pLastNode)

        pCurrent = node
        pCurrent.pLeft = pLastNode
        if pLastNode is not None:
            pLastNode.pRight = pCurrent
        pLastNode = pCurrent

        if node.pRight is not None:
            pLastNode = convertNode(node.pRight, pLastNode)
        return pLastNode

    if not isinstance(root, BinaryTreeNode) or root is None:
        return

    pLastNode = None
    pLastNode = convertNode(root, pLastNode)
    pHead = pLastNode
    while pHead is not None and pHead.pLeft is not None:
        pHead = pHead.pLeft
    return pHead


'''
Test Code Here
'''
def printTree(root):
    if root is None:
        return

    printTree(root.pLeft)
    print(root.val)
    printTree(root.pRight)

def printDoubledLinkedList(head):
    pNode = head
    print('The nodes from left to right are: ')
    while pNode is not None:
        print(pNode.val)

        if pNode.pRight is None:
            break
        pNode = pNode.pRight

    print('The nodes from right to left are: ')
    while pNode is not None:
        print(pNode.val)

        if pNode.pLeft is None:
            break
        pNode = pNode.pLeft
    print('\n')

#         10
#      /      \
#     6        14
#    /\        /\
#   4  8     12  16
def test1():
    A1 = BinaryTreeNode(10)
    A2 = BinaryTreeNode(6)
    A3 = BinaryTreeNode(14)
    A4 = BinaryTreeNode(4)
    A5 = BinaryTreeNode(8)
    A6 = BinaryTreeNode(12)
    A7 = BinaryTreeNode(16)

    A1.pLeft, A1.pRight = A2, A3
    A2.pLeft, A2.pRight = A4, A5
    A3.pLeft, A3.pRight = A6, A7

    print('Test1 begins: ')
    printTree(A1)

    head = convert(A1)
    print('The doubled Linked List: ')
    printDoubledLinkedList(head)


#              5
#             /
#            4
#           /
#          3
#         /
#        2
#       /
#      1
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

    print('Test2 begins: ')
    printTree(A1)

    head = convert(A1)
    print('The doubled Linked List: ')
    printDoubledLinkedList(head)

def test3():
    A1 = BinaryTreeNode(1)

    print('Test2 begins: ')
    printTree(A1)

    head = convert(A1)
    print('The doubled Linked List: ')
    printDoubledLinkedList(head)

if __name__ == '__main__':
    test1()
    test2()
    test3()