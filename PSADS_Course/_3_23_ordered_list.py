
class Node():
  def __init__(self, item):
    self.data = item
    self.next = None
  def get_data(self):
    return self.data
  def get_next(self):
    return self.next
  def set_data(self, new_data):
    self.data = new_data
  def set_next(self, new_next):
    self.next = new_next

class OrderedList():
  def __init__(self):
    self.head = None
  def is_empty(self):
    return self.head == None
  def size(self):
    current = self.head
    count = 0
    while current != None:
      current = current.get_next()
      count += 1
    return count
  def remove(self, item):
    previous = None
    current = self.head
    if self.is_empty():
      raise IndexError('remove from empty list')
    else:
      while current != None:
        if current.get_data() == item:
          if previous == None:
            self.head = current.get_next()  # if the first item was removed, head point to next
          else:
            previous.set_next(current.get_next())
          break
        else:
          previous = current
          current = current.get_next()
  def search(self, item):
    current = self.head
    found = False
    stop = False
    while current != None and not found and not stop:
      if current.get_data() == item:
        found = True
      elif current.get_data() > item:
        stop = True
      else:
        current = current.get_next()
    return found
  def add(self, item):
    temp = Node(item)
    previous = None
    current = self.head
    stop = False
    while current != None and not stop:
      if current.get_data() > item:
        stop = True
      else:
        previous = current
        current = current.get_next()
    if previous == None:
      self.head = temp
    else:
      previous.set_next(temp)
      temp.set_next(current)


my_list = OrderedList()
my_list.add(1)
my_list.add(2)
my_list.add(3)
my_list.remove(1)
print(my_list.size())
# print(my_list.remove(3))
# print(my_list.remove(1))
# print(my_list.size())
