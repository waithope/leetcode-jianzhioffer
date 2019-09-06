#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not isinstance(nums, list) or len(nums) == 0:
            return 0

        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and (dp[j] + 1) > dp[i]:
                    dp[i] = dp[j] + 1
        return max(dp)

