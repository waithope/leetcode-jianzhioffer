# -*- coding:utf-8 -*-
'''
    二叉树下一个节点
=========================
给定一颗二叉树和其中的一个节点，找出中序遍历序列的下一个节点，树中的节点除了
有两个分别指向左、右子节点的指针，还有一个指向父节点的指针。
'''

class TreeNode(object):
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


def getNextNode(node):
    '''
    三种情况：
    1.如果该节点有右子树，则右子树最左的节点就是node的下一个节点；
    2.如果该节点没有右子树，但是父节点的左子节点，则父节点是node下一个节点；
    3.如果该节点既没有右子树也不是父节点的左子节点，就沿着父节点指针向上回溯，
    找到某个是其父节点的左子节点的节点，则其父节点是node的下一个节点，如果回溯
    到根节点还没找到，则node没有下一个节点。
    '''
    if node is None:
        return

    if node.right:
        nextNode = node.right
        while nextNode.left:
            nextNode = nextNode.left
        return nextNode
    else:
        if node.parent and node == node.parent.left:
            return node.parent
        elif node.parent and node == node.parent.right:
            parent = node.parent
            while parent.parent:
                if parent == parent.parent.left:
                    return parent.parent
                parent = parent.parent
    return None


if __name__ == '__main__':
    n1 = TreeNode('a')
    n2 = TreeNode('b')
    n3 = TreeNode('c')
    n4 = TreeNode('d')
    n5 = TreeNode('e')
    n1.left, n2.parent = n2, n1
    n1.right, n3.parent = n3, n1
    n2.left, n4.parent = n4, n2
    n2.right, n5.parent = n5, n2
    print(getNextNode(n5).val == 'a')
    print(getNextNode(n3) == None)

