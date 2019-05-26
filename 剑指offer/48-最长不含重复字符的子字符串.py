# -*- coding:utf-8 -*-
'''
    最长不含重复字符的子字符串
===============================
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
假设字符串中只包含从'a'到'z'的字符。例如，在字符串"arabcacfr"中，最长的不含
重复字符的子字符串是"acfr"，长度为4。
'''

def longestSubstring(s):
    '''
    思路：从左往右扫描字符串，一并记录字符出现的位置和当前不重复字符串的长度
    curLength；如果当前字符之前已出现过，则进行如下判断：当前字符出现的位置
    和上一次该字符出现的位置距离是否大于当前不重复字符串的长度，如果是，表明
    在当前的子字符串中该字符并没有重复，则curLength加1；如果不是，表明当前
    字符串中该字符重复了，首先更新最长不重复字符串的长度为curLength(因为，
    下一步需要重置curLength)，然后将curLength重置为该字符的位置与其上一次
    出现的位置距离。
    '''
    if not isinstance(s, str) or len(s) == 0:
        return 0

    position = [-1] * 26
    curLength, maxLength = 0, 0

    for i in range(len(s)):
        prePos = position[ord(s[i]) - ord('a')]
        if prePos < 0 or (i - prePos) > curLength:
            curLength += 1
        else:
            if curLength > maxLength:
                maxLength = curLength
            curLength = i - prePos
        position[ord(s[i]) - ord('a')] = i

    if curLength > maxLength:
        maxLength = curLength
    return maxLength


import unittest

class TestLongestSubstring(unittest.TestCase):
    def test_longest_substring(self):
        self.assertEqual(longestSubstring("abcacfrar"), 4)
        self.assertEqual(longestSubstring("acfrarabc"), 4)
        self.assertEqual(longestSubstring("arabcacfr"), 4)
        self.assertEqual(longestSubstring("aaaa"), 1)
        self.assertEqual(longestSubstring("abcdefg"), 7)
        self.assertEqual(longestSubstring("aaabbbccc"), 2)
        self.assertEqual(longestSubstring("abcdaef"), 6)
        self.assertEqual(longestSubstring("a"), 1)
        self.assertEqual(longestSubstring(""), 0)


if __name__ == "__main__":
    unittest.main()