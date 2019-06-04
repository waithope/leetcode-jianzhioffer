

class avlNode(object):
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None

  def __str__(self):
    return str(self.key)

  def __repr__(self):
    return str(self.key)



class AVLTree(object):
  def __init__(self):
    self.node = None            # AVL tree attributes
    self.height = -1            # Take leave node's height as 0, so nil node's height is -1,
    self.balance = 0            # alternatively, nil node's height is 0, leave node 1

  def insert(self, key):
    temp = avlNode(key)

    if self.node is None:
      self.node = temp
      self.node.left = AVLTree()
      self.node.right = AVLTree()
    elif key < self.node.key:
      self.node.left.insert(key)
    elif key > self.node.key:
      self.node.right.insert(key)

    self.rebalance()

  def delete(self, key):
    if self.node is None:
      return

    if key < self.node.key:
      self.node.left.delete(key)
    elif key > self.node.key:
      self.node.right.delete(key)
    else:
      if self.node.left.node is None and self.node.right.node is None:   # target has no children
        self.node = None
      elif self.node.left.node is None:       # target has one children
        temp = self.node.right.node
        self.node = temp
        temp = None
      elif self.node.right.node is None:
        temp = self.node.left.node
        self.node = temp
        temp = None
      else:                                    # target has two children,
        successor = self.node.right.node       # find target key's successor and override it
        while successor.left.node:
          successor = successor.left.node

        self.node.key = successor.key
        self.delete(successor.key)

    self.rebalance()


  def rebalance(self):
    self.update_heights(recursive=False)
    self.update_balances(recursive=False)

    while self.balance < -1 or self.balance > 1:
      if self.balance < -1:
        if self.node.left.balance > 0:    # Left Right Case
          self.node.left.rotate_left()
          self.update_heights()
          self.update_balances()

        self.rotate_right()
        self.update_heights()
        self.update_balances()

      if self.balance > 1:
        if self.node.right.balance < 0:   # Right Left Case
          self.node.right.rotate_right()
          self.update_heights()
          self.update_balances()

        self.rotate_left()
        self.update_heights()
        self.update_balances()



  def update_heights(self, recursive=True):
    if self.node:
      if recursive:
        if self.node.left:
          self.node.left.update_heights()
        if self.node.right:
          self.node.right.update_heights()
      self.height = 1 + max(self.node.left.height, self.node.right.height)
    else:
      self.height = -1

  def update_balances(self, recursive=True):
    if self.node:
      if recursive:
        if self.node.left:
          self.node.left.update_balances()
        if self.node.right:
          self.node.right.update_balances()
      self.balance = self.node.right.height - self.node.left.height
    else:
      self.balance = 0

  def rotate_left(self):
    new_root = self.node.right.node
    old_root = self.node
    new_sub = new_root.left.node

    self.node = new_root
    new_root.left.node = old_root
    old_root.right.node = new_sub

  def rotate_right(self):
    new_root = self.node.left.node
    old_root = self.node
    new_sub = new_root.right.node

    self.node = new_root
    new_root.right.node = old_root
    old_root.left.node = new_sub

  def display(self, node=None, level=0):
    if node is None:
      node = self.node

    if node.right.node:
      self.display(node.right.node, level + 1)
      print('\t' * level, '    /')

    print('\t' * level, node)

    if node.left.node:
      print('\t' * level, '    \\')
      self.display(node.left.node, level + 1)


tree = AVLTree()
data = [1, 2, 3, 4, 5, 6, 7, 8]

for key in data:
  tree.insert(key)

# for key in [4,3]:
#     tree.delete(key)

# print(tree.inorder_traverse())
# tree.node.right.rotate_left()
tree.delete(5)
tree.display()