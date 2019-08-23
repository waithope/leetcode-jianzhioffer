#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # direct dfs method Time Limit Exceeded
        # self.res = 0
        # def dfs(nums, pos, sum_, target):
        #     if pos >= len(nums):
        #         if sum_ == target:
        #             self.res += 1
        #         return
        #     dfs(nums, pos+1, sum_+nums[pos], target)
        #     dfs(nums, pos+1, sum_-nums[pos], target)

        # dfs(nums, 0, 0, S)
        # return self.res

        memo = {}
        def dfs(nums, pos, sum_, target):
            if pos >= len(nums):
                if sum_ == target:
                    memo[(pos, sum_)] = 1
                else:
                    memo[(pos, sum_)] = 0

            if (pos, sum_) not in memo:
                memo[(pos, sum_)] = (dfs(nums, pos+1, sum_+nums[pos], target)
                                     + dfs(nums, pos+1, sum_-nums[pos], target))
            return memo[(pos, sum_)]
        return dfs(nums, 0, 0, S)

