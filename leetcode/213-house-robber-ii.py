#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
class Solution:
    def rob(self, nums: List[int]) -> int:
        def robCore(nums):
            memo = [0] * (len(nums) + 1)
            memo[1] = nums[0]
            for i in range(1, len(nums)):
                val = nums[i]
                memo[i + 1] = max(memo[i - 1] + val, memo[i])
            return memo[-1]

        if not isinstance(nums, list) or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        return max(robCore(nums[1:]), robCore(nums[:-1]))

