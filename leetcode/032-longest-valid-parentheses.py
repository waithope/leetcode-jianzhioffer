#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not isinstance(s, str) or len(s) == 0:
            return 0

        stack = [-1]
        longest = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    longest = max(longest, i - stack[-1])
        return longest

