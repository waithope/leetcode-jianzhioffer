

class Node(object):
  def __init__(self, key=None):
    self.key = key
    self.left = None
    self.right = None
    self.size = 1

# class Sentinel()

def is_same_tree(root1, root2):
  if root1 is None and root2 is None:
    return True
  if root1 is None or root2 is None:
    return False
  if root1.key == root2.key and is_same_tree(root1.left, root2.left) \
    and is_same_tree(root1.right, root2.right):
    return True
  return False

def insert(root, node):
  if root is sentinel:
    node.left = sentinel
    node.right = sentinel
    root = node
  else:
    if node.key < root.key:
        root.size += 1
        root.left = insert(root.left, node)
    else:
        root.size += 1
        root.right = insert(root.right, node)
  return root
def inorder_traverse(root):
  if root is None:
    return
  inorder_traverse(root.left)
  print(root.key, end=' ')
  inorder_traverse(root.right)
def preorder_traverse(root):
  if root is None:
    return
  print(root.key, end=' ')
  preorder_traverse(root.left)
  preorder_traverse(root.right)
def minimum_value_node(node):
  current = node
  while current.left is not None:
    current = current.left
  return current
def delete_node(root, key):
  if root is None:
    return root
  if key < root.key:
    root.left = delete_node(root.left, key)
  elif key > root.key:
    root.right = delete_node(root.right, key)
  else:
    if root.left is None:
      temp = root.right
      root = None
      return temp
    elif root.right is None:
      temp = root.left
      root = None
      return temp
    else:
      temp = minimum_value_node(root.right)
      root.key = temp.key
      root.right = delete_node(root.right, temp.key)
  return root

def display(root, level=0):
  if root.right is not sentinel:
    display(root.right, level + 1)
    print('\t' * level, "    /")

  print('\t' * level, "%d(%d)" %(root.key, root.size))

  if root.left is not sentinel:
    print('\t' * level, "    \\")
    display(root.left, level + 1)

def order_statistics(node, i):
  r = node.left.size + 1
  if i == r:
    return node
  elif i < r:
    node = order_statistics(node.left, i)
  else:
    node = order_statistics(node.right, i - r)
  return node





sentinel = Node()
sentinel.size = 0
root = sentinel
root = insert(root, Node(70))
root = insert(root, Node(50))
root = insert(root, Node(80))
root = insert(root, Node(0))
root = insert(root, Node(10))
root = insert(root, Node(75))
root = insert(root, Node(90))
root = insert(root, Node(72))

display(root)
# print(root.right.key)
os_node = order_statistics(root, 5)
print(os_node.key)

# inorder_traverse(root)

# print('\n')
# root = delete_node(root, 50)
# root = delete_node(root, 0)
# root = delete_node(root, 0)
# root = delete_node(root, 10)
# root = delete_node(root, 80)
# root = delete_node(root, 70)

# inorder_traverse(root)







# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)

# print(root.key, root.left.key, root.right.key, root.left.left.key)

