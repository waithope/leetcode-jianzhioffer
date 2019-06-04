

class Stack():
  def __init__(self):
    self.items = []
  def is_empty(self):
    return self.items == []
  def push(self, item):
    self.items.append(item)
  def pop(self):
    return self.items.pop()
  def peek(self):
    return self.items[len(self.items) - 1]
  def size(self):
    return len(self.items)

# new_stack = Stack()
# new_stack.push('cat')
# new_stack.push('dog')
# new_stack.push(9)
# new_stack.push(True)
# new_stack.pop()
# print(new_stack.peek())
# print(new_stack.items)
# print(new_stack.is_empty())

# def reverse_str(input_str):
#   temp_str = Stack()
#   myStr = ''
#   for ch in input_str:
#     temp_str.push(ch)
#   while not temp_str.is_empty():
#     myStr += temp_str.pop()
#   # for i in range(len(input_str)):
#     # myStr += input_str[len(input_str)-1 - i]
#   return myStr

# print(reverse_str('messi123456'))

# def paren_checker(symbol_str):
#   s = Stack()
#   is_balanced = True
#   pos = 0
#   while pos < len(symbol_str) and is_balanced:
#     symbol = symbol_str[pos]
#     if symbol in '({[':
#       s.push(symbol)
#     else:
#       if s.is_empty():
#         is_balanced = False
#       else:
#         top = s.pop()
#         if not ('({['.index(top) == ')}]'.index(symbol)):
#           is_balanced = False
#     pos += 1
#   if is_balanced and s.is_empty():
#     return True
#   else:
#     return False

# print(paren_checker('{[(]}'))


# def base_conversion(num, base):
#   digits = '0123456789ABCDE'
#   s = Stack()
#   binary_str = ''
#   while num > 0:
#     remainder = num % base
#     s.push(remainder)
#     num //= base
#   while not s.is_empty():
#     binary_str += digits[(s.pop())]
#   return binary_str

# print(base_conversion(26, 16))