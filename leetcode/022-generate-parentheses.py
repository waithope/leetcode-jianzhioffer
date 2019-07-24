#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(leftRemain, rightRemain, s, res):
            if leftRemain > rightRemain or leftRemain < 0 or rightRemain < 0:
                return

            if leftRemain == 0 and rightRemain == 0:
                res.append(s)

            dfs(leftRemain - 1, rightRemain, s + '(', res)
            dfs(leftRemain, rightRemain - 1, s + ')', res)

        if not isinstance(n, int) or n < 1:
            return []

        s, res = '', []
        dfs(n, n, s, res)
        return res

