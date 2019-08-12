#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
from copy import deepcopy
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not isinstance(nums, list) or len(nums) == 0:
            return []

        # method 1: recursive
        # def permutation(nums, res, idx):
        #     if idx == len(nums):
        #         res.append(deepcopy(nums))

        #     for i in range(idx, len(nums)):
        #         nums[i], nums[idx] = nums[idx], nums[i]
        #         permutation(nums, res, idx + 1)
        #         nums[i], nums[idx] = nums[idx], nums[i]

        # res = []
        # permutation(nums, res, 0)
        # return res

        # method 2: deep fisrt search
        def dfs(nums, path, res, visited):
            if len(path) == len(nums):
                res.append(path)

            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    dfs(nums, path+[nums[i]], res, visited)
                    visited[i] = False

        res = []
        visited = [False] * len(nums)
        dfs(nums, [], res, visited)
        return res


