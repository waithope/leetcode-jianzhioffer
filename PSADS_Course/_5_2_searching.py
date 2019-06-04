

def insert_sort(input_list):

  for i in range(1, len(input_list)):
    key = input_list[i]
    j = i - 1
    while input_list[j] > key and j >= 0:   # compare element must use key not input_list[i]
      input_list[j + 1] = input_list[j]
      j -= 1
    input_list[j + 1] = key
  return input_list

import random
# print(insert_sort([random.randrange(60) for i in range(20)]))


## Dynamic Programming Rod-cut problem ##
price = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

def max(l, r):
  if l < r:
    return r
  else:
    return l

def cut_rod_recur(p, n):
  if n == 0:
    return 0
  q = -1
  for i in range(1, n + 1):
    # every loop record current max q and return back to original problem when loop terminates
    q = max(q, p[i] + cut_rod_recur(p, n - i))
  return q



def cut_rod_top_down(p, n, revenue):
  if revenue[n] >= 0:
    return revenue[n]
  elif n == 0:
    return 0
  else:
    q = -1
    for i in range(1, n + 1):
      q = max(q, p[i] + cut_rod_top_down(p, n - i, revenue))
  revenue[n] = q
  return q

# print(cut_rod_top_down(price, 10, [-1]*11))

## The difference between top-down approach is bottom-up approach has less cost of recursive calls
def cut_rod_bottom_up(p, n, revenue):
  revenue[0] = 0
  for i in range(1, n + 1):
    q = -1
    for j in range(1, i + 1):
      q = max(q, p[j] + revenue[i-j])
    revenue[i] = q
  return revenue[n]

# print(cut_rod_bottom_up(price, 10, [-1]*11))
# import timeit
# t = timeit.timeit("cut_rod_bottom_up([0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30], 10, [-1]*11)", "from __main__ import cut_rod_bottom_up", number=100)
# print("it takes %f secs" % t)
def cut_rod_bottom_up_extend(p, n):
  revenue = [-1]*(n+1)
  revenue[0] = 0
  length = [0]*(n+1)
  for i in range(1, n + 1):
    q = -1
    for j in range(1, i + 1):
      if q < p[j] + revenue[i-j]:
        q = p[j] + revenue[i-j]
        length[i] = j
    revenue[i] = q
  return revenue, length

def print_cut_rod(p, n):
  r, l = cut_rod_bottom_up_extend(p, n)
  while n > 0:
    print(l[n])
    n = n - l[n]

# print_cut_rod(price, 7)


def binary_search(order_list, item):
  low = 0
  high = len(order_list) - 1
  found = False
  while low <= high and not found:
    mid = (low + high) // 2
    if order_list[mid] == item:
      found = True
    elif order_list[mid] < item:
      low = mid + 1
    elif order_list[mid] > item:
      high = mid - 1
  return found

# print(binary_search([1, 3, 5, 7, 9, 11, 13], 8))

