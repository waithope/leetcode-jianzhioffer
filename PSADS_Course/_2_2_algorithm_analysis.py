
# import time

# def sum_of_n2(n):
#   start = time.time()

#   sum = 0;
#   for i in range(1, n+1):
#     sum += i
#   # return sum
#   end = time.time()
#   return sum, end-start

# for i in range(5):
#   print("Sum is %d required %10.7f seconds" % sum_of_n2(10000))

##### Self Check #####
def find_min_n2(input_list):
  list_min = input_list[0]
  for i in input_list:
    is_min = True
    for j in input_list:
      if i > j:
        is_min = False
    if is_min:
      list_min = i
  return list_min

def find_min_n(input_list):
  list_min = input_list[0]
  for i in range(len(input_list)):
    if input_list[i] < list_min:
      list_min = input_list[i]
  return list_min

import random
import time
for list_size in range(100000, 1000001, 100000):
  input_list = [random.randrange(100000) for number in range(list_size)]
  start = time.time()
  print(find_min_n(input_list))
  end = time.time()
  print("List size: %d required seconds %.7f" % (list_size, end-start))

# print(find_min_n())
# print(find_min_n2())