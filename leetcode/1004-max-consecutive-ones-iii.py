#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        if not isinstance(A, list) or not isinstance(K, int):
            return 0
        maxLen, start, zeros = 0, 0, 0
        for i in range(len(A)):
            if A[i] != 1:
                zeros += 1
            while zeros > K:
                if A[start] != 1:
                    zeros -= 1
                start += 1
            maxLen = max(maxLen, i - start + 1)
        return maxLen

