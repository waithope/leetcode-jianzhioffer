# -*- coding:utf-8 -*-
'''
    数字在排序数组中出现的次数
==============================
统计一个数字在排序数组中出现的次数。例如输入排序数组{1, 2, 3, 3,3, 3, 4, 5}和
数字3，由于3在这个数组中出现了4次，因此输出4。
'''

def getNumberOfK(nums, k):
    '''
    思路：由于数组是已排序好的，只要找到第一个k的位置a和最后一个k的位置b，就可以得到
    k在数组中出现的次数b-a+1。
    时间效率O(logn)
    '''
    def getFirstK(nums, k):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == k:
                if mid == 0 or nums[mid - 1] != k:
                    return mid
                else:
                    end = mid - 1
            elif nums[mid] < k:
                start = mid + 1
            else:
                end = mid - 1
        return None

    def getLastK(nums, k):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == k:
                if (mid == len(nums) - 1) or (nums[mid + 1] != k):
                    return mid
                else:
                    start = mid + 1
            elif nums[mid] < k:
                start = mid + 1
            else:
                end = mid - 1
        return None

    if not isinstance(nums, list) or len(nums) == 0:
        return 0

    indexOfFirstK = getFirstK(nums, k)
    indexOfLastK = getLastK(nums, k)
    if indexOfFirstK is None or indexOfLastK is None:
        return 0
    else:
        return indexOfLastK - indexOfFirstK + 1


import unittest

class TestGetNumberOfK(unittest.TestCase):
    def test_get_number_of_k(self):
        self.assertEqual(getNumberOfK([1,2,3,3,3,3,4,5], 3), 4)
        self.assertEqual(getNumberOfK([3,3,3,3,4,5], 3), 4)
        self.assertEqual(getNumberOfK([1,2,3,3,3,3], 3), 4)
        self.assertEqual(getNumberOfK([1,3,3,3,3,4,5], 2), 0)
        self.assertEqual(getNumberOfK([1,3,3,3,3,4,5], 2), 0)
        self.assertEqual(getNumberOfK([3,3,3,3], 3), 4)
        self.assertEqual(getNumberOfK([3,3,3,3], 3), 4)
        self.assertEqual(getNumberOfK([3], 3), 1)
        self.assertEqual(getNumberOfK(None, 0), 0)


if __name__ == '__main__':
    unittest.main()