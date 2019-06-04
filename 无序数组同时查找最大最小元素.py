# -*- coding:utf-8 -*-
'''
    无序数组同时查找最大最小元素
=================================
给定一个长度为n的无序序列，同时查找出这个序列中的最大和最小值，要求比较次数最小。
'''

def findMaxAndMin(nums):
    '''
    思路：如果只是在无序序列中查找最大或最小值，至少需要n-1次比较，但是同时
    查找出最大值和最小值却不需要2(n-1)次比较，而只需要1.5n次比较。其策略是：
    将n个数据按2个一组进行分组，每组两个数进行比较得到较大值和较小值，
    '''
    if not isinstance(nums, list) or len(nums) == 0:
        return

    size = len(nums)
    maxNum, minNum = 0, 0
    index = 0
    if size % 2 == 0:
        if nums[0] < nums[1]:
            minNum = nums[0]
            maxNum = nums[1]
        else:
            minNum = nums[1]
            maxNum = nums[0]
        index = 2
    else:
        minNum = maxNum = nums[0]
        index = 1

    while index < size - 1:
        if nums[index] < nums[index + 1]:
            minNum = min(minNum, nums[index])
            maxNum = max(maxNum, nums[index + 1])
        else:
            minNum = min(minNum, nums[index + 1])
            maxNum = max(maxNum, nums[index])
        index += 2
    return [minNum, maxNum]



import unittest

class TestFindMaxAndMin(unittest.TestCase):
    def test_find_max_and_min(self):
        self.assertEqual(findMaxAndMin([]), None)
        self.assertEqual(findMaxAndMin([2]), [2, 2])
        self.assertEqual(findMaxAndMin([2, -1]), [-1, 2])
        self.assertEqual(findMaxAndMin([2,1,8,8,7,6,-2,2]), [-2, 8])



if __name__ == '__main__':
    unittest.main()

