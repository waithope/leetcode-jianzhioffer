

class Node():
  def __init__(self, init_data):
    self.data = init_data
    self.next = None
  def get_data(self):
    return self.data
  def get_next(self):
    return self.next
  def set_data(self, new_data):
    self.data = new_data
  def set_next(self, new_next):
    self.next = new_next


# my_node = Node('messi')
# print(my_node.get_data())

class LinkedList():
  def __init__(self):
    self.head = None
  def is_empty(self):
    return self.head == None
  def add(self, item):
    temp = Node(item)
    temp.set_next(self.head)
    self.head = temp
  def size(self):
    current = self.head
    count = 0
    while current != None:
      current = current.get_next()
      count += 1
    return count
  def search(self, item):
    current = self.head
    found = False
    while current != None and not found:
      if current.get_data() == item:
        found = True
      else:
        current = current.get_next()
    return found
  def remove(self, item):
    previous = None
    current = self.head
    if current == None:
      return
      # raise ValueError("Linked list is empty")
    while current != None:
      if current.get_data() == item:
        if previous == None:
          self.head = current.get_next()
          current = None
        else:
          previous.set_next(current.get_next())
          current = None
        break
      else:
        previous = current
        current = current.get_next()
  ## TODO implement following methods
  def append(self, item):
    temp = Node(item)
    current = self.head
    if self.is_empty():
      self.head = temp
    else:
      while current.get_next() != None:
          current = current.get_next()
      current.set_next(temp)
  def index(self, item):
    item_index = 0
    current = self.head
    found = False
    while current != None and not found:
      item_index += 1
      if current.get_data() == item:
        found = True
      else:
        current = current.get_next()
    if found == True:
      return item_index
    else:
      raise ValueError("%s is not in the linked list" % item)
  def insert(self, pos, item):
    # temp = Node(item)
    # previous = None
    # current = self.head
    # count = 0
    if pos <= 1:
      self.add(item)
    elif pos > self.size():
      self.append(item)
    else:
      temp = Node(item)
      previous = None
      current = self.head
      count = 1
      while count < pos:
        previous = current
        current = current.get_next()
        count += 1
      previous.set_next(temp)
      temp.set_next(current)
  def pop(self):
    previous = None
    current = self.head
    if self.is_empty():
      raise IndexError("pop from empty list")
    else:
      while current.get_next() != None:
        previous = current
        current = current.get_next()
      data = current.get_data()
      if current == self.head:
        self.head = current.get_next()
      else:
        previous.set_next(current.get_next())
      return data
  def pop_from(self, pos):
    if pos == self.size():
      data = self.pop()
    elif pos > self.size():
      raise IndexError("pop out of range")
    elif pos <= 1:
      data = self.head.get_data()
      self.head = self.head.get_next()
    else:
      previous = None
      current = self.head
      count = 1
      while count < pos:
        previous = current
        current = current.get_next()
        count += 1
      data = current.get_data()
      previous.set_next(current.get_next())
    return data
  def reverse(self): ## there is two ways to reverse a single list:
    prev = None     ## iterative and recursive method
    curr = self.head
    while(curr != None):
      next = curr.get_next()
      curr.set_next(prev)
      # next.set_next(curr) ## note that when do this next node lost the next node he points to
      prev = curr
      curr = next
    self.head = prev




# my_list = LinkedList()
# my_list.append(17)
# my_list.append(21)
# my_list.append(33)
# my_list.append(43)
# my_list.append(53)

# my_list.reverse()
# print("my list is reversed:")
# for i in range(my_list.size()):
#   print(my_list.pop())


## Doubly Linked List
class DLNode():
  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None
  def get_prev(self):
    return self.prev
  def get_next(self):
    return self.next
  def get_data(self):
    return self.data
  def set_data(self, new_data):
    self.data = new_data
  def set_next(self, next):
    self.next = next
  def set_prev(self, prev):
    self.prev = prev

class DoublyList():
  def __init__(self):
    self.head = None
    self.tail = None
  def add(self, item):    ## always add node at the front
    temp = DLNode(item)
    temp.set_next(self.head)
    temp.set_prev(None)

    if self.head != None:
      self.head.set_prev(temp)
    else:
      self.tail = temp

    self.head = temp
  def insert_after(self, prev_node, data):  ## Add a node after a given node
    if prev_node == None:
      raise ValueError("the given previous node cannot be None")
    new_node = DLNode(data)
    new_node.set_next(prev_node.get_next())
    prev_node.set_next(new_node)
    new_node.set_prev(prev_node)
    if new_node.get_next() != None:
      new_node.get_next().set_prev(new_node)
    else:
      self.tail = new_node
  def append(self, data):
    new_node = DLNode(data)
    curr = self.head
    if curr == None:
      self.head = new_node
      self.tail = new_node
      return
    while curr.get_next() != None:
      curr = curr.get_next()
    curr.set_next(new_node)
    new_node.set_prev(curr)
    self.tail = new_node
  def remove(self, node):
    if node.get_prev() == None:
      self.head = node.get_next()
    else:
      node.get_prev().set_next(node.get_next())
    if node.get_next() == None:
      self.tail = node.get_prev()
    else:
      node.get_next().set_prev(node.get_prev())




L = DoublyList()
L.append(1)
L.append('dog')
L.append('cat')
# L.append("a brand new")
# L.append('holly')
# L.add(8)
# L.insert_after(L.head, 9)
# L.insert_after(L.head.get_next(), 9.5)
# print(L.head.get_next().get_next().get_next().get_next().get_data())
print(L.tail.get_data())