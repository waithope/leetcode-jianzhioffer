
import queue

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTree(preorder, inorder):
    def helper(left, right):
        if left < right:
            node = TreeNode(preorder.pop())
            # ind splits the tree to left subtree and right subtree
            ind = index[node.val]
            node.left = helper(left, ind)
            node.right = helper(ind+1, right)
            return node

    index = {val: i for i, val in enumerate(inorder)}
    preorder.reverse()
    return helper(0, len(preorder))


def printTreeHierarchical(root, res):
    if root is None:
        return

    queueTree = queue.Queue()
    queueTree.put(root)
    currentLevel = 1
    nextLevel = 0
    while not queueTree.empty():
        node = queueTree.get()
        res.append(node.val)
        currentLevel -= 1

        if node.left is not None:
            queueTree.put(node.left)
            nextLevel += 1
        if node.right is not None:
            queueTree.put(node.right)
            nextLevel += 1

        if currentLevel == 0:
            currentLevel = nextLevel
            nextLevel = 0


if __name__ == '__main__':
    n = int(input().strip())
    preorder = list(map(int, input().strip().split()))
    root = buildTree(preorder, sorted(preorder))
    res = []
    printTreeHierarchical(root, res)
    print(' '.join(map(str, res)))
