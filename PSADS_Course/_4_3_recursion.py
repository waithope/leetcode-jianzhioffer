

def list_sum(num_list):
  total_sum = 0
  for num in num_list:
    total_sum += num
  return total_sum


# print(list_sum([1, 3, 5, 7, 9]))
total_sum = 0
def sum_recur_v1(num_list, index):
  global total_sum
  if index < len(num_list):
    total_sum += num_list[index]
    index += 1
    return sum_recur_v1(num_list, index)
  else:
    return total_sum

# print(sum_recur_v1([1], 0))

def sum_recur_v2(num_list):
  if len(num_list) == 1:
    return num_list[0]
  else:
    return num_list[0] + sum_recur_v2(num_list[1:])

# print(sum_recur_v2([1, 3, 5, 7, 9]))

def int_to_str_recur(num, base):
  cvt_str = '0123456789ABCDEF'
  if num < base:
    return cvt_str[num]
  else:
    return int_to_str_recur(num // base, base) + cvt_str[num % base]

print(int_to_str_recur(255, 2))

from _3_5_stack import Stack

res_stack = Stack()
def int_to_str(num, base):
  cvt_str = "0123456789ABCDEF"
  while num > 0:
    if num < base:
      res_stack.push(cvt_str[num])
    else:
      res_stack.push(cvt_str[num % base])
    num //= base
  res_str = ''
  while not res_stack.is_empty():
    res_str += res_stack.pop()
  return res_str

# print(int_to_str(255, 16))


def rev_str(src_str):
  if len(src_str) == 1:
    return src_str[0]
  else:
    return rev_str(src_str[1:]) + src_str[0]

# print(rev_str('hello, world'))

import string
def del_white_space(comp_str):
  new_str = ''
  for char in comp_str:
    if char in string.punctuation or char == ' ':
      continue
    else:
      new_str += char
  return new_str

# print(del_white_space("Go hang a salami; I'm a lasagna hog."))

def pal_checker(test_str):
  bkwd_str = rev_str(test_str)
  match = True
  index = 0
  for ch in test_str:
    if ch == bkwd_str[index]:
      index += 1
    else:
      match = False
      break
  return match
# print(pal_checker(del_white_space("Go hang a salami; I'm a lasagna hog")))
# print(pal_checker(del_white_space("Go hang a salami; I'm a lasagna hog".lower())))
# print(pal_checker(del_white_space("Wassamassaw".lower())))
