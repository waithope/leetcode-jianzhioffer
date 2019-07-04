import unittest
'''
              4Sum
===================================
Given an array nums of n integers and an integer target,
are there elements a, b, c, and d in nums such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.
Note:
The solution set must not contain duplicate quadruplets.
Example:
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
sorted nums = [-2, -1, 0, 0, 1, 2]
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''


def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    if len(nums) < 4:
        return []

    nums.sort()
    res = []
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, len(nums)-2):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            k = j + 1
            z = len(nums) - 1
            while k < z:
                s = nums[i] + nums[j] + nums[k] + nums[z]
                if s == target:
                    res.append([nums[i], nums[j], nums[k], nums[z]])
                    while k < z and nums[k] == nums[k+1]:
                        k += 1
                    while k < z and nums[z] == nums[z-1]:
                        z -= 1
                    k += 1
                    z -= 1
                elif s < target:
                    k += 1
                else:
                    z -= 1
    return res


class Test_4Sum(unittest.TestCase):
    def test_4sum(self):
        self.assertEqual(fourSum([], 0), [])
        self.assertEqual(fourSum([1, 0, -1, 0, -2, 2], 0),
                         [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]])


if __name__ == '__main__':
    unittest.main()
