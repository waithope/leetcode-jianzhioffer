#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not isinstance(strs, list) or len(strs) == 0:
            return ''

        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if ch != other[i]:
                    return shortest[:i]
        return shortest

