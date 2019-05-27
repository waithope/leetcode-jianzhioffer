# -*- coding:utf-8 -*-
'''
    数组中数值与下标相等的元素
==============================
假设一个单调递增的数组里的每个元素都是整数并且是唯一的。请编程实现一个函数找出
数组中任意一个数值等于其下标的元素。例如，在数组{-3,-1,1,3,5}中，数字3和它的
下标相等。
'''

def findNumSameAsIndex(nums):
    '''
    思路：由于数组中的元素是单调递增的且唯一，因此还是利用二分查找的思想，如果
    mid对应的元素值与下标相等，直接返回，如果不相等且元素值大于下标，则在前半
    部分进行二分查找；如果不相等且元素值小于下标值，则在后半部分进行二分查找。
    '''
    if not isinstance(nums, list) or len(nums) == 0:
        return None

    start, end = 0, len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == mid:
            return mid
        elif nums[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    return None


import unittest

class TestFindNumSameAsIndex(unittest.TestCase):
    def test_find_num_same_as_index(self):
        self.assertEqual(findNumSameAsIndex(None), None)
        self.assertEqual(findNumSameAsIndex([0]), 0)
        self.assertEqual(findNumSameAsIndex([10]), None)
        self.assertEqual(findNumSameAsIndex([-3,-1,1,3,5]), 3)
        self.assertEqual(findNumSameAsIndex([0,1,3,5,6]), 0)
        self.assertEqual(findNumSameAsIndex([-1,0,1,2,4]), 4)
        self.assertEqual(findNumSameAsIndex([-1,0,1,2,5]), None)


if __name__ == '__main__':
    unittest.main()