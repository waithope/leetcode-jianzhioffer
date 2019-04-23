# -*- coding:utf-8 -*-
'''
    连续子数组的最大和
=========================
输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。
求所有子数组的和的最大值。要求时间复杂度为O(n)
'''


def maxSubarray1(nums):
    '''
    思路：我们用一个变量记录连续子数组的最大和，一个变量记录每个阶段的累加和。
    从数组第一个位置开始逐个累加，每进行一次累加之后将累加和与最大和进行比较，
    更新最大和。当累加和小于当前位置数字本身时，就说明前一个阶段的连续子数组
    的和会小于从当前位置开始的子数组的和，所以抛弃之前的累加和，更新当前累加
    和为当前数字。按照上述步骤，直到遍历完数组为止。
    '''
    if not isinstance(nums, list) or len(nums) <= 0:
        return

    maxSum = -(2**32)
    curSum = 0
    for num in nums:
        curSum += num
        if curSum < num:
            curSum = num
        if curSum > maxSum:
            maxSum = curSum
    return maxSum


def maxSubarray2(nums):
    if not isinstance(nums, list) or len(nums) <= 0:
        return
    dc = [0 for i in range(len(nums))]
    dc[0] = nums[0]
    maxSum = nums[0]
    for i in range(1, len(nums)):
        dc[i] = max(nums[i], nums[i] + dc[i-1])
        if dc[i] > maxSum:
            maxSum = dc[i]
    return maxSum



import unittest

class TestMaxSubArray(unittest.TestCase):
    def test_max_sub_array(self):
        self.assertEqual(maxSubarray1([1,-2,3,10,-4,7,2,-5]), 18)
        self.assertEqual(maxSubarray1([-2,-8,-1,-5,-9]), -1)
        self.assertEqual(maxSubarray1([2,8,1,5,9]), 25)
        self.assertEqual(maxSubarray1(None), None)
        self.assertEqual(maxSubarray2([1,-2,3,10,-4,7,2,-5]), 18)
        self.assertEqual(maxSubarray2([-2,-8,-1,-5,-9]), -1)
        self.assertEqual(maxSubarray2([2,8,1,5,9]), 25)
        self.assertEqual(maxSubarray2(None), None)


if __name__ == '__main__':
    unittest.main()
