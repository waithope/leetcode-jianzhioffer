# -*- coding:utf-8 -*-
'''
    旋转数组的最小数字
========================
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增
排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组{3, 4, 5, 1, 2}为
{1, 2, 3, 4, 5}的一个旋转，该数组的最小值为1。
'''

def findMinInRotatedArray(nums):
    '''
    类似书中的思路
    最坏情况时间复杂度为O(n)
    '''
    def findMinInOrder(arr):
        result = arr[0]
        for num in arr:
            if num < result:
                result = num
        return result

    if not isinstance(nums, list) or len(nums) <= 0:
        return

    left, right = 0, len(nums) - 1
    while (right - left) > 1:
        if nums[left] < nums[right]:
            return nums[left]
        mid = left + (right - left) // 2
        if nums[left] == nums[right] == nums[mid]:
            return findMinInOrder(nums[left:right+1])

        if nums[mid] >= nums[left]:
            left = mid
        else:
            right = mid
    return min(nums[left], nums[right])

def findMinInRotatedArray2(nums):
    '''
    另一种实现思路
    最坏情况下时间复杂度依然为O(n)
    '''
    left, right = 0, len(nums) - 1
    while left < right:
        while left < right and nums[left] == nums[left+1]:
            left += 1
        while right > left and nums[right] == nums[right-1]:
            right -= 1

        if left == right:
            return nums[left]

        mid = left + (right - left) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]


import unittest

class TestFindMinimum(unittest.TestCase):
    def test_find_minimum(self):
        self.assertEqual(findMinInRotatedArray([1]), 1)
        self.assertEqual(findMinInRotatedArray([3, 1, 2]), 1)
        self.assertEqual(findMinInRotatedArray([2,2,2,0,1]), 0)
        self.assertEqual(findMinInRotatedArray([1,0,1,1,1,1]), 0)
        self.assertEqual(findMinInRotatedArray2([1]), 1)
        self.assertEqual(findMinInRotatedArray2([3, 1, 2]), 1)
        self.assertEqual(findMinInRotatedArray2([2,2,2,0,1]), 0)
        self.assertEqual(findMinInRotatedArray2([1,0,1,1,1,1]), 0)

if __name__ == '__main__':
    unittest.main()