# -*- coding:utf-8 -*-
'''
    数组中出现次数超过一半的数字
================================
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如，输入一个
长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长
度的一半，因此输出2。
'''
import random
def partition(nums, start, end):
    if not isinstance(nums, list) or len(nums) <= 0 \
        or start < 0 or end >= len(nums):
        return -1

    index = random.randint(start, end)
    nums[index], nums[end] = nums[end], nums[index]
    small = start - 1
    for i in range(start, end+1):
        if nums[i] < nums[end]:
            small += 1
            if small != i:
                nums[small], nums[i] = nums[i], nums[small]

    small += 1
    nums[small], nums[end] = nums[end], nums[small]
    return small

def moreThanHalfNum1(nums):
    '''
    解法一：时间效率O(n)，需要修改原数组
    如果一个数字的出现次数超过一半，也就是将数组进行排序后，中间位置
    所对应的数字就是答案。但是将数组进行排序时间效率是O(nlgn)，有没有O(n)的
    方法呢。答案是有的，从上面可以看出，我们并不需要对整个数组进行排序，只需要
    找到排序后中间位置的值就好了，所以题目可以简化成，用快排的partition函数
    寻找分割位置的index，如果index刚好为中间位置middle，就直接返回index
    对应的值；如果index小于middle，则partition在index+1, end之间找；如果
    index大于middle，则partition在0, index-1之间找；重复以上过程。最后对
    返回的值进行统计，如果确实出现次数超过一半，直接返回，否则返回None。
    '''
    if not isinstance(nums, list) or len(nums) <= 0:
        return None

    length = len(nums)
    middle = length // 2
    start, end = 0, length - 1
    index = partition(nums, start, end)
    while index != middle:
        if index > middle:
            end = index - 1
            index = partition(nums, start, end)
        else:
            start = index + 1
            index = partition(nums, start, end)
    result = nums[middle]
    if nums.count(result) > middle:
        return result
    else:
        return

def moreThanHalfNum2(nums):
    '''
    解法二：如果一个数字出现的次数超过数组长度的一半，也就是他的次数比其他数组
    出现的次数总和还要多。利用这个特点，我们可以在遍历数组的时候保存两个值，一
    个是数字本身，另一个是次数。当遍历到下一个数字时，如果下一个数字与保存的数
    字相等，则次数加一，如果不相等，则次数减一。如果次数为0，则保存下一个数字，
    并设置次数为1。当遍历完成后，要找的数字就是最后一次设置次数为1时保存的数字。
    时间效率O(n)
    '''
    if not isinstance(nums, list) or len(nums) <= 0:
        return
    candidate, count = None, 0
    for num in nums:
        if candidate == num:
            count += 1
        elif count == 0:
            candidate = num
            count = 1
        else:
            count -= 1

    if nums.count(candidate) > (len(nums) // 2):
        return candidate
    else:
        return

import unittest

class TestMoreThanHalfNum(unittest.TestCase):
    def test_more_than_half_num(self):
        self.assertEqual(moreThanHalfNum1([1,2,3,2,2,2,5,4,2]), 2)
        self.assertEqual(moreThanHalfNum1([1,2,3,2,4,2,5,2,3]), None)
        self.assertEqual(moreThanHalfNum1([2,2,2,2,2,1,3,4,5]), 2)
        self.assertEqual(moreThanHalfNum1([2,2,2,2,2,1,3,4,5]), 2)
        self.assertEqual(moreThanHalfNum1(None), None)
        self.assertEqual(moreThanHalfNum2([1,2,3,2,2,2,5,4,2]), 2)
        self.assertEqual(moreThanHalfNum2([1,2,3,2,4,2,5,2,3]), None)
        self.assertEqual(moreThanHalfNum2([2,2,2,2,2,1,3,4,5]), 2)
        self.assertEqual(moreThanHalfNum2([2,2,2,2,2,1,3,4,5]), 2)
        self.assertEqual(moreThanHalfNum2(None), None)



if __name__ == '__main__':
    unittest.main()

