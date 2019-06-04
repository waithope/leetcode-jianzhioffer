

class Deque():
  def __init__(self):
    self.items = []
  def add_front(self, item):
    self.items.append(item)
  def add_rear(self, item):
    self.items.insert(0, item)
  def remove_front(self):
    return self.items.pop()
  def remove_rear(self):
    return self.items.pop(0)
  def size(self):
    return len(self.items)
  def is_empty(self):
    return self.items == []


# new_deque = Deque()
# new_deque.add_front('dog')
# new_deque.add_front('cat')
# new_deque.add_rear('elephant')
# new_deque.remove_front()
# new_deque.remove_rear()
# new_deque.remove_front()
# print(new_deque.is_empty())

def palnd_checker(test_str):
  char_deque = Deque()

  for ch in test_str:
    char_deque.add_front(ch)

  still_match = True
  while char_deque.size() > 1 and still_match:
    left_char = char_deque.remove_rear()
    right_char = char_deque.remove_front()

    if left_char != right_char:
      still_match = False

  return still_match


print(palnd_checker('gotootog'))