#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
class Solution:
    def isValid(self, s: str) -> bool:
        if not isinstance(s, str):
            return False
        if len(s) == 0:
            return True

        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []
        for char in s:
            if char in '([{':
                stack.append(char)
            else:
                if len(stack) == 0 or pairs[char] != stack.pop():
                    return False
        if len(stack) == 0:
            return True
        return False

