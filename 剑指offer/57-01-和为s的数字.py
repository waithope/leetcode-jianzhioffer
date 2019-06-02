# -*- coding:utf-8 -*-
'''
        和为s的数字
============================
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。
如果有多对数字的和等于s，输出任意一对即可。例如，输入数组{1,2,4,7,11,15}
和数字15。由于4+11=15，因此输出4和11。
'''

def findNumsWithSum(nums, target):
    '''
    思路：首先想到的一个方法就是固定一个数字，在数组中寻找和这个数字加起来和为target
    的数字，但是这个方法的时间效率是O(n^2)，一个更好的方法是用两个指针，一个指针指向
    数组中的第一个元素，第二个指针是指向数组中的最后一个元素，如果指向的两个数字和大于
    target，就将第二个指针向前移动一个位置；如果指向的两个数组和小于target，就将第
    一个指针向后移动一个位置，直到找到位置。
    '''
    if (not isinstance(nums, list) or len(nums) == 0
        or not isinstance(target, int)):
        return None

    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [nums[left], nums[right]]
        elif s > target:
            right -= 1
        else:
            left += 1
    return None


import unittest

class TestFindNumsWithSum(unittest.TestCase):
    def test_find_nums_with_sum(self):
        self.assertEqual(findNumsWithSum([1,2,4,7,11,15], 15), [4, 11])
        self.assertEqual(findNumsWithSum([1,2,4,7,11,16], 17), [1, 16])
        self.assertEqual(findNumsWithSum([1,2,4,7,11,16], 10), None)
        self.assertEqual(findNumsWithSum(None, 10), None)


if __name__ == '__main__':
    unittest.main()