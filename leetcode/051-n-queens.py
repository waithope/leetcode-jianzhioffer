#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isValid(nums, n):
            for i in range(n):
                if abs(nums[i] - nums[n]) == n - i or nums[i] == nums[n]:
                    return False
            return True

        def dfs(nums, index, path, res):
            if index == len(nums):
                res.append(path)
                return

            for i in range(len(nums)):
                nums[index] = i
                if isValid(nums, index):
                    string = '.' * len(nums)
                    dfs(nums, index + 1, path+[string[:i] + 'Q' + string[i+1:]], res)

        if not isinstance(n, int) or n < 1:
            return []

        nums, res = [-1] * n, []
        dfs(nums, 0, [], res)
        return res
