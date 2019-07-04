import unittest
'''
    Search in Rotated Sorted Array
======================================
Suppose an array sorted in ascending order is rotated at some pivot
unknown to you beforehand. (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search.
If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''


def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    l, h = 0, len(nums)-1

    while l <= h:
        m = (l+h) // 2
        if nums[m] == target:
            return m
        elif nums[l] <= nums[m]:
            if nums[l] <= target <= nums[m]:
                h = m - 1
            else:
                l = m + 1
        else:
            if nums[m] <= target <= nums[h]:
                l = m + 1
            else:
                h = m - 1
    return -1


class TestSearchInRotatedSortedArray(unittest.TestCase):
    def test_search_in_rotated_sorted_array(self):
        self.assertEqual(search([3, 1], 1), 1)
        self.assertEqual(search([5, 1, 3], 5), 0)
        self.assertEqual(search([4, 5, 6, 7, 0, 1, 2], 0), 4)
        self.assertEqual(search([4, 5, 6, 7, 0, 1, 2], 3), -1)
        self.assertEqual(search([6, 7, 8, 9, 10, 1, 2], 2), 6)


if __name__ == '__main__':
    unittest.main()
