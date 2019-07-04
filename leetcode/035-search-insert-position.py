'''
    Search Insert Position
==============================
Given a sorted array and a target value, return the index
if the target is found. If not, return the index
where it would be if it were inserted in order.
You may assume no duplicates in the array.
Input: [1,3,5,6], 5
Output: 2

Input: [1,3,5,6], 2
Output: 1

Input: [1,3,5,6], 7
Output: 4

Input: [1,3,5,6], 0
Output: 0
'''


import unittest


def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    l, h = 0, len(nums) - 1
    while l < h:
        m = (l + h) // 2
        if target == nums[m]:
            return m
        elif target > nums[m]:
            l = m + 1
        else:
            h = m - 1
    if target <= nums[l]:
        return l
    return l+1

    # Solution 2
    # return len([x for x in nums if x < target])


class TestSearchInsertPosition(unittest.TestCase):
    def test_search_insert(self):
        self.assertEqual(searchInsert([1], 0), 0)
        self.assertEqual(searchInsert([1, 2], 0), 0)
        self.assertEqual(searchInsert([1, 3, 5, 6], 5), 2)
        self.assertEqual(searchInsert([1, 3, 5, 6], 2), 1)
        self.assertEqual(searchInsert([1, 3, 5, 6], 7), 4)
        self.assertEqual(searchInsert([1, 3, 5, 6], 0), 0)


if __name__ == '__main__':
    unittest.main()
