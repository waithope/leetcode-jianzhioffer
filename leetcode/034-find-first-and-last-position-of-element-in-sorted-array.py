import unittest
'''
    Find First and Last Position of Element in Sorted Array
===============================================================
Given an array of integers nums sorted in ascending order,
find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [], target = 0
Output: [-1, -1]

Example 2:
Input: nums = [1], target = 1
Output: [0, 0]

Example 3:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 4:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''


def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # if not nums:
    #    return [-1, -1]
    #
    #left, right = 0, len(nums) - 1
    #res = [-1]*2
    # while left < right:
    #    mid = left + (right - left) // 2
    #    if nums[mid] < target:
    #        left = mid + 1
    #    else:
    #        right = mid
    #
    # if nums[left] != target:
    #    return res
    # else:
    #    res[0] = left
    #
    #right = len(nums) - 1
    # while left < right:
    #    mid = left + (right - left) // 2 + 1  # make mid biased to the right instead left
    #    if nums[mid] > target:
    #        right = mid - 1
    #    else:
    #        left = mid
    #res[1] = right
    # return res

    def binarySearchLeft(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def binarySearchRight(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return right

    l, r = binarySearchLeft(nums, target), binarySearchRight(nums, target)
    return [l, r] if l <= r else [-1]*2


class TestSearchRange(unittest.TestCase):
    def test_search_range(self):
        self.assertEqual(searchRange([], 0), [-1, -1])
        self.assertEqual(searchRange([1], 1), [0, 0])
        self.assertEqual(searchRange([5, 7, 7, 8, 8, 10], 8), [3, 4])
        self.assertEqual(searchRange([5, 7, 7, 8, 8, 10], 6), [-1, -1])


if __name__ == '__main__':
    unittest.main()
