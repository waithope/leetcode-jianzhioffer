#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not isinstance(s, str) or not isinstance(k, int):
            return

        maxCount, start, res = 0, 0, 0
        dic = {}
        for i in range(len(s)):
            dic[s[i]] = dic.get(s[i], 0) + 1
            # 更新当前窗口的字符出现的最大频次
            maxCount = max(maxCount, dic[s[i]])
            # 如果当前窗口需要修改的字符多余k，则缩小窗口大小1个字符
            if i - start + 1 - maxCount > k:
                dic[s[start]] -= 1
                start += 1
            res = max(res, i - start + 1)
        return res
