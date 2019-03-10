# -*- coding='utf-8' -*-
'''
    Find Minimum in Rotated Sorted Array II
================================================
Suppose an array sorted in ascending order is rotated at some pivot
unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.
The array may contain duplicates.
Example 1:
Input: [1,3,5]
Output: 1

Example 2:
Input: [2,2,2,0,1]
Output: 0
'''

def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
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

import unittest

class TestFindMinimum(unittest.TestCase):
    def test_find_minimum(self):
        self.assertEqual(findMin([1]), 1)
        self.assertEqual(findMin([3, 1, 2]), 1)
        self.assertEqual(findMin([2,2,2,0,1]), 0)
        self.assertEqual(findMin([1,0,1,1,1,1]), 0)
        self.assertEqual(findMin([1,1,1,1,0,1]), 0)
        self.assertEqual(findMin([3, 4, 5, 1, 2]), 1)
        self.assertEqual(findMin([4, 5, 6, 7, 0, 1, 2]), 0)

if __name__ == '__main__':
    unittest.main()
