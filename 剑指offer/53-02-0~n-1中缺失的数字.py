# -*- coding:utf-8 -*-
'''
    0~n-1中缺失的数字
=========================
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0到n-1之内。
在范围0到n-1的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
'''


def getMissingNum(nums):
    '''
    思路：假设n个数字中没有缺失的数字，那么数组下标0就对应数字0，数组下标n-1就对应
    数字n-1。因此，可以通过二分查找的方法，定位数组中第一个数字和下标不相等的地方，
    而这个下标值就是对应的缺失数字。
    '''
    if not isinstance(nums, list) or len(nums) == 0:
        return -1

    start, end = 0, len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] != mid:
            if mid == 0 or nums[mid - 1] == mid - 1:
                return mid
            else:
                end = mid - 1
        else:
            start = mid + 1
    if start == len(nums):
        return len(nums)
    else:
        return -1


import unittest

class TestGetMissingNum(unittest.TestCase):
    def test_get_missing_num(self):
        self.assertEqual(getMissingNum([1]), 0)
        self.assertEqual(getMissingNum([0]), 1)
        self.assertEqual(getMissingNum([1,2,3,4,5]), 0)
        self.assertEqual(getMissingNum([0,1,2,3,4]), 5)
        self.assertEqual(getMissingNum([0,1,2,4,5]), 3)


if __name__ == '__main__':
    unittest.main()