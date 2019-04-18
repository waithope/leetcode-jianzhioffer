# -*- coding:utf-8 -*-
'''
    复杂链表的复制
====================
请实现函数complexListClone(head)，复制一个复杂链表。在复杂链表中，每个节点除了
有一个pNext指针指向下一个节点，还有一个pSibling指针指向链表中的任意节点或者None。
        -----------------
       \|/              |
A-------B-------C-------D-------E  |
|       |      /|\             /|\ |
--------+--------               |  |
        -------------------------
链表节点定义如下：
class ComplexListNode(object):
    def __init__(self, val, pNext=None, pSibling=None):
        self.val = val
        self.pNext = pNext
        self.pSibling = pSibling
'''

class ComplexListNode(object):
    def __init__(self, val, pNext=None, pSibling=None):
        self.val = val
        self.pNext = pNext
        self.pSibling = pSibling


def complexListClone(head):
    '''
    思路1: 分两步，第一步复制原始链表上的节点N创建节点N'，然后把创建出来的节点
    用pNext连接起来，同时把<N, N'>配对信息保存到一个哈希表中；第二步，原始链表
    N节点的pSibling是节点S，则N'节点的pSibling应该为S'，通过在哈希表中找到
    <S, S'>配对信息就可以设置新链表的pSibling节点。
    该方法的时间复杂度为O(N), 空间复杂度为O(N)

    思路2：分三步，第一步复制原始链表上的节点N并创建节点N'，将N'链接到N的后面；
    第二步，将N'的pSibling链接到N.pNext；第三步，将上两步得到的链表拆分成
    两个链表，一个链表由总链表的奇数位置的节点组成，一个链表由总链表的偶数为止的
    节点组成。
    该方法的时间复杂度为O(N)，空间复杂度为O(1)
    '''
    def cloneNodes(head):
        pNode = head
        while pNode is not None:
            pClonedNode = ComplexListNode(pNode.val)
            pClonedNode.pNext = pNode.pNext
            pNode.pNext = pClonedNode
            pNode = pClonedNode.pNext

    def connectSiblingNode(head):
        pNode = head
        while pNode is not None:
            pClonedNode = pNode.pNext
            if pNode.pSibling is not None:
                pClonedNode.pSibling = pNode.pSibling.pNext
            pNode = pClonedNode.pNext

    def splitList(head):
        pNode = head
        pClonedHead = None
        pClonedNode = None
        if pNode is not None:
            pClonedHead = pNode.pNext
            pClonedNode = pClonedHead
            pNode.pNext = pClonedNode.pNext
            pNode = pNode.pNext
        while pNode is not None:
            pClonedNode.pNext = pNode.pNext
            pClonedNode = pClonedNode.pNext
            pNode.pNext = pClonedNode.pNext
            pNode = pNode.pNext
        return pClonedHead

    cloneNodes(head)
    connectSiblingNode(head)
    return splitList(head)



'''
Test Code Here
'''
def printList(head):
    pNode = head
    while pNode is not None:
        print('The node val is: ', pNode.val)
        pNode = pNode.pNext
    print('PrintList ends.')

#           -----------------
#          \|/              |
#   1-------2-------3-------4-------5
#   |       |      /|\             /|\
#   --------+--------               |
#           -------------------------
def test1():
    A1 = ComplexListNode(1)
    A2 = ComplexListNode(2)
    A3 = ComplexListNode(3)
    A4 = ComplexListNode(4)
    A5 = ComplexListNode(5)

    A1.pNext, A1.pSibling = A2, A3
    A2.pNext, A2.pSibling = A3, A5
    A3.pNext = A4
    A4.pNext, A4.pSibling = A5, A2

    print('Test1: ')
    print('The original List is: ')
    printList(A1)

    pClonedHead = complexListClone(A1)
    print('The cloned List is: ')
    printList(pClonedHead)

#  m_pSibling指向结点自身
#           -----------------
#          \|/              |
#   1-------2-------3-------4-------5
#          |       | /|\           /|\
#          |       | --             |
#          |------------------------|
def test2():
    A1 = ComplexListNode(1)
    A2 = ComplexListNode(2)
    A3 = ComplexListNode(3)
    A4 = ComplexListNode(4)
    A5 = ComplexListNode(5)

    A1.pNext = A2
    A2.pNext, A2.pSibling = A3, A5
    A3.pNext, A3.pSibling = A4, A3
    A4.pNext, A4.pSibling = A5, A2

    print('Test2: ')
    print('The original List is: ')
    printList(A1)

    pClonedHead = complexListClone(A1)
    print('The cloned List is: ')
    printList(pClonedHead)

def test3():
    A1 = ComplexListNode(1)

    A1.pSibling = A1

    print('Test3: ')
    print('The original List is: ')
    printList(A1)

    pClonedHead = complexListClone(A1)
    print('The cloned List is: ')
    printList(pClonedHead)

if __name__ == '__main__':
    test1()
    test2()
    test3()