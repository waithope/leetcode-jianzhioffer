# -*- coding:utf-8 -*-
'''
    Regular Expression Matching
===================================
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
'''


def isMatch(self, s: str, p: str) -> bool:
    '''
    参考：https://leetcode.com/problems/regular-expression-matching/discuss/5723/My-DP-approach-in-Python-with-comments-and-unittest
    matches[i][j] means the match status between p[:i] and s[:j], i.e.
    matches[0][0] means the match status of two empty strings, and
    matches[1][1] means the match status of p[0] and s[0].
    '''
    if not isinstance(s, str) or not isinstance(p, str):
        return

    m, n = len(p), len(s)
    matches = [[False] * (n + 1) for _ in range(m + 1)]

    # 当p和s为空字符串时，适配
    matches[0][0] = True

    # 当s为空的状态时，且p字符串当前为'*'时，对matches进行更新
    for i in range(2, m + 1):
        matches[i][0] = matches[i - 2][0] and (p[i - 1] == '*')

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # p字符串当前位置字符不为'*'时的情况
            if p[i - 1] != '*':
                matches[i][j] = (matches[i - 1][j - 1]
                                    and (p[i - 1] == s[j - 1] or p[i - 1] == '.'))
            else:
                # p字符串当前字符为'*'时，且对前一个字符取0次
                matches[i][j] = matches[i - 2][j]

                # p字符串当前字符为'*'时，对前一个字符取1次
                if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                    matches[i][j] |= matches[i][j - 1]
    return matches[-1][-1]
