

from random import randint
import timeit
from random import randrange
import time


def bubble_sort(a_list):
    for passes_num in range(len(a_list)-1, 0, -1):
        for i in range(passes_num):
            if a_list[i] > a_list[i+1]:
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
                # a_list[i] ^= a_list[i+1]
                # a_list[i+1] ^= a_list[i]
                # a_list[i] ^= a_list[i+1]
    return a_list


l = [i for i in range(2000, 0, -1)]
# bubble_sort(l)


def short_bubble_sort(a_list):
    is_sorted = False
    passes_num = len(a_list) - 1
    while passes_num > 0 and not is_sorted:
        is_sorted = True
        for i in range(passes_num):
            if a_list[i] > a_list[i+1]:
                is_sorted = False
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
        passes_num -= 1
    return a_list


# start = time.time()
# # bubble_sort(l)
# short_bubble_sort(l)
# end = time.time()
# print('it takes %s secs' % str(end-start))
# print('it takes %f secs' % timeit.timeit('bubble_sort([i for i in range(1000,0,-1)])', 'from __main__ import bubble_sort,randrange', number=10))

# print('it takes %f secs' % timeit.timeit('short_bubble_sort([i for i in range(1000,0,-1)])', 'from __main__ import short_bubble_sort,randrange', number=10))

# print(len(l))
# print(l)
# print(short_bubble_sort(l))


def selection_sort(a_list):
    for fill_slot in range(len(a_list)-1, 0, -1):
        pos_of_max = 0
        for pos in range(fill_slot):
            if a_list[pos+1] > a_list[pos_of_max]:
                pos_of_max = pos + 1
        a_list[pos_of_max], a_list[fill_slot] = a_list[fill_slot], a_list[pos_of_max]
    return a_list

# print(selection_sort([randrange(100) for i in range(10)]))


def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        key = a_list[index]
        while index > 0 and key < a_list[index-1]:
            a_list[index] = a_list[index - 1]
            index -= 1
        a_list[index] = key
    return a_list

# print(insertion_sort([i for i in range(30, -2, -1)]))


def shell_sort(a_list):
    gap = len(a_list) // 2    # increment sequence
    while gap > 0:
        for pos in range(gap, len(a_list)):
            # for pos in range(start_pos+gap, len(a_list), gap):
            key = a_list[pos]
            while pos >= gap and key < a_list[pos - gap]:
                a_list[pos] = a_list[pos-gap]
                pos -= gap
            a_list[pos] = key
        gap //= 2
    return a_list


# print(shell_sort([randrange(300) for num in range(50)]))
# l = [num for num in range(4000, 0, -1)]
# start = time.time()

# shell_sort(l)
# end = time.time()
# print(end-start)
# print('It takes %f secs' % timeit.timeit('shell_sort(l)', 'from __main__ import shell_sort,randrange, l', number=10))


def merge(a_list, l, m, h):
    n1 = m-l+1
    n2 = h-m
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = a_list[l+i]    # origin index l+i is the key to get first halve sublist
    for j in range(0, n2):
        # origin index m+1 is the key to get second halve sublist
        R[j] = a_list[m+1+j]
    # L = a_list[l:l+n1]
    # R = a_list[m+1:m+1+n2]

    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            a_list[k] = L[i]
            i += 1
        else:
            a_list[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        a_list[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        a_list[k] = R[j]
        j += 1
        k += 1


def merge_sort(a_list, l, h):
    if l < h:
        m = (l + h)//2
        merge_sort(a_list, l, m)
        merge_sort(a_list, m+1, h)
        merge(a_list, l, m, h)

# unsorted_list = [9, 8, 7, 3, 4, 4, 5, 4, 3, 2, 1, 0]
# merge_sort(unsorted_list, 0, len(unsorted_list)-1)
# print(unsorted_list)


def partition(a_list, l, h):
    pivot = a_list[h]
    smaller_index = l - 1

    for pos in range(l, h):
        if a_list[pos] <= pivot:
            smaller_index += 1
            a_list[smaller_index], a_list[pos] = a_list[pos], a_list[smaller_index]
    a_list[smaller_index+1], a_list[h] = a_list[h], a_list[smaller_index+1]
    return smaller_index + 1


def quick_sort(a_list, l, h):
    if l < h:
        partition_index = partition(a_list, l, h)
        quick_sort(a_list, l, partition_index-1)
        quick_sort(a_list, partition_index+1, h)

# lst = [randrange(100) for num in range(20)]
# quick_sort(lst, 0, len(lst) - 1)
# print(lst)


# 3-way quick sort using Dutch National Flag Problem Algorithm
def partition_dnf(a_list, l, h, li, mj):
    if h-l <= 1:
        if a_list[h] < a_list[l]:
            a_list[h], a_list[l] = a_list[l], a_list[h]
            h -= 1
            l += 1
        li = l
        mj = h

    pivot = a_list[h]
    li = l
    mj = l
    while mj <= h:
        if a_list[mj] < pivot:
            # move item smaller than pivot to
            a_list[li], a_list[mj] = a_list[mj], a_list[li]
            li += 1                                        # the left
            mj += 1
        elif a_list[mj] == pivot:
            mj += 1
        elif a_list[mj] > pivot:
            a_list[mj], a_list[h] = a_list[h], a_list[mj]
            h -= 1
    return li - 1, mj


def quick_sort_dnf(a_list, l, h):
    li = None   # low index
    mj = None   # mid index
    if l < h:
        li, mj = partition_dnf(a_list, l, h, li, mj)
        quick_sort_dnf(a_list, l, li)
        quick_sort_dnf(a_list, mj, h)

# l = [4, 9, 4, 4, 1, 9, 4, 4, 9, 4, 4, 1, 4]
# quick_sort_dnf(l, 0, len(l)-1)
# print(l)


def quick_sort_random(a_list, l, h):
    if l == h:  # handle empty list
        return
    left = l
    right = h
    pivot_index = randint(left, right)
    pivot = a_list[pivot_index]

    while left < right:
        while a_list[left] < pivot:
            left += 1
        while a_list[right] > pivot:
            right -= 1
        if left <= right:
            if left < right:
                a_list[left], a_list[right] = a_list[right], a_list[left]
            left += 1
            right -= 1

    if left < h:
        quick_sort_random(a_list, left, h)
    if right > l:
        quick_sort_random(a_list, l, right)


l = [6, 6, 6, 6, 3, 3]
quick_sort_random(l, 0, len(l)-1)
print(l)


# Heap sort

def max_heapify(a_list, size, i):
    l = (i << 1) + 1
    r = (i << 1) + 2

    if l < size and a_list[l] > a_list[i]:
        largest = l
    else:
        largest = i
    if r < size and a_list[r] > a_list[largest]:
        largest = r
    if largest != i:
        a_list[i], a_list[largest] = a_list[largest], a_list[i]
        max_heapify(a_list, size, largest)


def heap_sort(a_list, size):
    # build max heap
    for pos in range((size//2)-1, -1, -1):  # size is tricky here, be careful
        max_heapify(a_list, len(a_list), pos)

    for i in range(size-1, 0, -1):
        a_list[0], a_list[i] = a_list[i], a_list[0]
        # size -= 1
        max_heapify(a_list, i, 0)


# l = [randrange(100) for num in range(30)]
# # l = [9, 8, 7, 6, 5, 4, 3, 3, 2, 2, 2, 1, 0]
# heap_sort(l, len(l))
# print(l)

# Method to make an unstable algorithm stable
# A = [9, 8, 4, 4, 3]
# A2 = [(y, x) for x, y in enumerate(A, 1)]
# print(A2)


# Priority queue
class Node():
    def __init__(self, obj, key):
        self.obj = obj
        self.key = key


class PriorityQueue():
    def __init__(self, a_list):
        self.a_list = a_list
        self.Build_Max_Heap()

    def __len__(self):
        return len(self.a_list)

    def Build_Max_Heap(self):
        for i in range(len(self.a_list)//2-1, -1, -1):
            self.Max_Heapify(i)

    def Max_Heapify(self, index):
        l = (index << 1) + 1
        r = (index << 1) + 2
        if l < len(self.a_list) and self.a_list[l].key > self.a_list[index].key:
            largest = l
        else:
            largest = index
        if r < len(self.a_list) and self.a_list[r].key > self.a_list[largest].key:
            largest = r
        if largest != index:
            self.a_list[largest], self.a_list[index] = self.a_list[index], self.a_list[largest]
            self.Max_Heapify(largest)

    def Heap_Maximum(self):
        return self.a_list[0]

    def Heap_Extract(self):
        if len(self.a_list) < 1:
            raise IndexError("heap underflow")
        max = self.a_list[0]
        self.a_list[0] = self.a_list.pop()
        self.Max_Heapify(0)
        return max

    def Heap_Increase_Key(self, index, new_key):
        if new_key < self.a_list[index].key:
            raise ValueError("new key is smaller than current key")
        self.a_list[index].key = new_key
        pi = index // 2
        while index > 0 and self.a_list[pi].key < self.a_list[index].key:
            self.a_list[pi], self.a_list[index] = self.a_list[index], self.a_list[pi]
            index = pi
            pi = index // 2


# a_list = []
# a_list.append(Node('a', 5))
# a_list.append(Node('c', 1))
# a_list.append(Node('z', 10))
# a_list.append(Node('b', 2))
# a_list.append(Node('d', 20))
# heap_pq = PriorityQueue(a_list)
# # print(len(heap_pq))
# heap_pq.Heap_Increase_Key(3, 13)
# for item in heap_pq.a_list:
#   print(item.obj, item.key)
# print(heap_pq.Heap_Extract().key)


# Counting sort

# Integer
def counting_sort(a_list, scope):
    output = [0]*(len(a_list))
    count = [0]*scope
    for num in a_list:
        count[num] += 1
    for i in range(1, scope):
        count[i] += count[i-1]

    for j in range(len(a_list)-1, -1, -1):
        output[count[a_list[j]] - 1] = a_list[j]
        count[a_list[j]] -= 1  # this step is important
    return output

# print(counting_sort([randrange(30) for num in range(50)], 256))
# Char


def counting_sort_char(a_str, scope):
    output = [0]*(len(a_str))
    count = [0]*scope
    for ch in a_str:
        count[ord(ch)] += 1
    for i in range(1, scope):
        count[i] += count[i-1]
    for j in range(len(a_str)-1, -1, -1):
        output[count[ord(a_str[j])] - 1] = a_str[j]
        count[ord(a_str[j])] -= 1
    return ''.join(output)

# print(counting_sort_char("geeksforgeeks", 256))


# Radix sort

def get_max(a_list):
    max_num = a_list[0]
    for num in a_list:
        if max_num < num:
            max_num = num
    return max_num


def counting_sort_radix(a_list, exp):
    output = [0]*len(a_list)
    count = [0]*(10)
    for num in a_list:
        # index = (num % exp)//(exp//10)
        index = num // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i-1]

    for j in range(len(a_list)-1, -1, -1):
        index = a_list[j] // exp
        output[count[index % 10] - 1] = a_list[j]
        count[index % 10] -= 1
    a_list[:] = output[:]
    # print('assignment:', a_list)
    # print(a_list)
    # print(a_list)
    # for i in range(0, len(a_list)):
    #   a_list[i] = output[i]


def radix_sort(a_list):
    max = get_max(a_list)
    exp = 1
    while max//exp > 0:
        counting_sort_radix(a_list, exp)
        exp *= 10
        # print('function return:')
        # print(a_list)

# l = [170, 45, 75, 90, 802, 24, 2, 66]
# l = [randrange(300) for num in range(50)]
# radix_sort(l)
# print(l)


# Bucket Sort
def bucket_sort(arr):
    n = len(arr)
    max = get_max(arr)
    bucket = [[] for i in range(n)]
    for num in arr:
        # get the position of num relative to max
        bucket[n*num//(max + 1)].append(num)

    for i in range(len(bucket)):
        if len(bucket[i]) > 1:
            insertion_sort(bucket[i])

    output = []
    for j in range(n, -1, -1):
        while len(bucket[j]) > 0:
            output.append(bucket[j].pop())

    arr[:] = output[:]

# l = [randrange(20) for num in range(30)]
# bubble_sort(l)
# print(l)
