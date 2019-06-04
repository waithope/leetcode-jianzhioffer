

def list_test1():
  l = []
  for i in range(1000):
    l = l + [i]

def list_test2():
  l = []
  for i in range(1000):
    l.append(i)

def list_test3():
  l = [i for i in range(1000)]

def list_test4():
  l = list(range(1000))

import timeit
print("concatenation:")
print(timeit.timeit('list_test1()', 'from __main__ import list_test1', number=100))
# print(timeit.Timer('list_test1()', 'from __main__ import list_test1').timeit(100))
print("append:")
print(timeit.timeit('list_test2()', 'from __main__ import list_test2', number=100))
# print(timeit.Timer('list_test2()', 'from __main__ import list_test2').timeit(100))
print("comprehension:")
print(timeit.timeit('list_test3()', 'from __main__ import list_test3', number=100))
# print(timeit.Timer('list_test3()', 'from __main__ import list_test3').timeit(100))
print("list_range:")
print(timeit.timeit('list_test4()', 'from __main__ import list_test4', number=100))
# print(timeit.Timer('list_test4()', 'from __main__ import list_test4').timeit(100))

# x = list(range(10000))
# print(timeit.timeit('x.pop(0)', 'from __main__ import x', number = 1000))
# print(timeit.timeit('x.pop()', 'from __main__ import x', number = 1000))