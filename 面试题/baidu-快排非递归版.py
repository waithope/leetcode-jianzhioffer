# -*- coding:utf-8 -*-
'''
    快排非递归版
===================
'''
import random
def partition(nums, left, right):
    if left < 0 or right >= len(nums):
        return -1

    index = random.randint(left, right)
    nums[index], nums[right] = nums[right], nums[index]
    small = left - 1
    for i in range(left, right + 1):
        if nums[i] < nums[right]:
            small += 1
            if small != i:
                nums[small], nums[i] = nums[i], nums[small]
    small += 1
    nums[small], nums[right] = nums[right], nums[small]
    return small

def quickSort_Iteratively(nums):
    '''
    思路：利用栈的思想，将需要继续排序的首尾下标存入栈中，不断弹栈进行分区操作
    '''
    if not isinstance(nums, list) or len(nums) == 0:
        return
    if len(nums) < 2:
        return nums

    left, right = 0, len(nums) - 1
    stack = [right, left]
    while len(stack) != 0:
        left = stack.pop()
        right = stack.pop()
        index = partition(nums, left, right)
        if left < index - 1:
            stack.append(index - 1)
            stack.append(left)
        if right > index + 1:
            stack.append(right)
            stack.append(index + 1)


# test1
if __name__ == '__main__':
    data1 = [0,-1,-8,10,11,5,6]
    quickSort_Iteratively(data1)
    assert(data1 == [-8,-1,0,5,6,10,11])
    # test2
    data2 = [5,4,3,2,1,0,-1,-2]
    quickSort_Iteratively(data2)
    assert(data2 == [-2,-1,0,1,2,3,4,5])
    # test3
    data3 = [1,1,1,2,2,2,0,0,0,-1,-1,-1]
    quickSort_Iteratively(data3)
    assert(data3 == [-1,-1,-1,0,0,0,1,1,1,2,2,2])
    # test4
    data4 = [13,4,12,1,14,11,7,3,9,10,5,2,6,8]
    quickSort_Iteratively(data4)
    assert(data4 == [1,2,3,4,5,6,7,8,9,10,11,12,13,14])


