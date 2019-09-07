#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if not isinstance(haystack, str) or not isinstance(needle, str):
        #     return -1

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

        # KMP算法，时间复杂度O(m + n), 空间复杂度O(n)
        # def getNext(_next, pattern):
        #     i, j = 0, -1
        #     _next[0] = -1
        #     while i < len(pattern):
        #         if j == -1 or pattern[i] == pattern[j]:
        #             i += 1
        #             j += 1
        #             _next[i] = j
        #         else:
        #             j = _next[j]

        # def KMP(string, pattern, _next):
        #     i, j = 0, 0
        #     while j < len(pattern) and i < len(string):
        #         if j == -1 or string[i] == pattern[j]:
        #             i += 1
        #             j += 1
        #         else:
        #             j = _next[j]
        #     if j == len(pattern): #如果匹配，j指针指向len(pattern)
        #         return i - j
        #     else:
        #         return -1

        # _next = [0] * (len(needle) + 1)
        # getNext(_next, needle)
        # return KMP(haystack, needle, _next)

