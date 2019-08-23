#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#
class Solution:
    def decodeString(self, s: str) -> str:
        if not isinstance(s, str) or len(s) == 0:
            return ''

        curNum, curStr = 0, ''
        stack = []
        for c in s:
            if c.isdigit():
                curNum = 10 * curNum + ord(c) - ord('0')
            elif c == '[':
                stack.append(curNum)
                stack.append(curStr)
                curNum = 0
                curStr = ''
            elif c == ']':
                string = stack.pop()
                num = stack.pop()
                curStr = string + curStr * num
            else:
                curStr += c
        return curStr
