#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
class Solution:
    def climbStairs(self, n: int) -> int:
        if not isinstance(n, int) or n < 1:
            return 0

        result = [1, 2]
        if n <= 2:
            return result[n - 1]

        cur = 2
        pre = 1
        for i in range(3, n + 1):
            fibo = cur + pre
            pre =  cur
            cur = fibo
        return fibo
