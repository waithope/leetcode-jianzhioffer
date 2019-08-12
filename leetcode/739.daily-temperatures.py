#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not isinstance(T, list) or len(T) == 0:
            return []

        stack = []
        res = [0] * len(T)
        for i, num in enumerate(T):
            while stack and T[stack[-1]] < num:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res


