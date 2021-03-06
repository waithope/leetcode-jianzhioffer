#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not isinstance(nums, list) or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        memo = [0] * (len(nums) + 1)
        memo[1] = nums[0]
        for i in range(1, len(nums)):
            val = nums[i]
            memo[i + 1] = max(val + memo[i - 1], memo[i])
        return memo[-1]

