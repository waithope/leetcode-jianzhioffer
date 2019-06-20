# -*- coding:utf-8 -*-
'''
    最长回文子串
===================
Given a string s, find the longest palindromic substring in s.
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
'''

def longestPalindrome_DP(s):
    '''
    思路：利用动态规划的方法来寻找最长回文子串，字符串中位置i到j要是回文子串
    要满足如下公式：P(i+1, j-1) = True and s[i] == s[j]
    时间复杂度O(n^2)，空间复杂度O(n)
    '''
    if not isinstance(s, str) or len(s) == 0:
        return

    max_i, max_j, maxLen = 0, 0, 0
    size = len(s)
    dp = [[False] * size, [False] * size]
    for i in range(size - 1, -1, -1):
        for j in range(i, size):
            if i == j:
                dp[0][j] = True
            elif j == i + 1:
                dp[0][j] = (s[i] == s[j])
            else:
                dp[0][j] = (dp[1][j-1] and (s[i] == s[j]))
            if dp[0][j] and (j - i + 1) > maxLen:
                max_i, max_j, maxLen = i, j, j - i + 1
        dp[0], dp[1] = dp[1], dp[0]
    return s[max_i:max_j+1]


def longestPalindrome_Manacher(s):
    '''
    思路：manacher方法解决了动态规划方法存在的两个问题，一个是长度奇偶性带来的
    对称轴位置问题以及重复访问的问题。manacher算法首先对字符串做预处理，在每个
    字符中间插入同样的一个符号（这个符号不在原串中出现），这样使得所得的串是奇数
    长度。
    假设处理后的字符串如下：
    S：# A # B # A # C # A # B #
    P：1 2 1 2 1 2 1 6 1 2 1 2 1
    P[i]表示以s[i]字符为中心的回文串的半径长度，即以s[i]为中心的回文串对折的长度。
    manacher算法的目的就是要计算这个数组，为了计算除这个数组还需要两个辅助变量，一
    个变量为maxRight表示当前访问的所有回文子串中所能触及到的最右一个字符的位置，另
    一个变量center表示maxRight代表的回文子串的中心。假设我们已经处理到前i-1个P数组
    中的值，现在需要求第i个值。若此时i小于marRight，说明以i为中心的回文串至少有一部分
    包含在目前maxRight代表的回文子串中。由于i之前的值已经计算出，定位i关于center对称
    的位置j，即2*center - i。P[j]是已经在之前的访问中计算得到了，因此以i为中心的回
    文串长度至少为min(P[j], maxRight-i)，原因是i，j是关于center对称的，所以j的回文
    串可以对应为i的回文串，只要在maxRight范围内就可以。由于目前得到的以i为中心的回文串
    的边界在maxRight之内，所以下一步还要继续扩展i的边界，找到以i为中心的最大回文串。当
    i在maxRight的右边时，以i为对称轴的回文串还没有任何一个部分被访问过，于是只能从i的
    左右两边开始尝试扩展了，当左右两边字符不同，或者到达字符串边界时停止。
    参考博客：https://blog.csdn.net/thinkerleo1997/article/details/78167401
    https://segmentfault.com/a/1190000003914228
    https://leetcode.com/problems/longest-palindromic-substring/discuss/3337/Manacher-algorithm-in-Python-O(n)

    时间复杂度O(n)，空间复杂度O(n)
    '''
    if not isinstance(s, str) or len(s) == 0:
        return

    T = '#{}#'.format('#'.join(s))
    n = len(T)
    P = [0] * n
    centerIndex, maxRight = 0, 0
    for i in range(n):
        if i < maxRight:
            P[i] = min(maxRight - i, P[2 * center - i])
        else:
            P[i] = 1          # 回文串半径算上自身的长度
        while ((i - P[i]) >= 0
                and (i + P[i]) < n
                and T[i - P[i]] == T[i + P[i]]):
                P[i] += 1
        if P[i] + i > maxRight:
            center = i
            maxRight = i + P[i] - 1
    maxLen, centerIndex = max((l, i) for i, l in enumerate(P))
    return s[(centerIndex - (maxLen - 1))//2: (centerIndex + (maxLen - 1))//2]


import unittest

class TestLongestPalinSubstring(unittest.TestCase):
    def test_longest_palindromic_substirng(self):
        self.assertIn(longestPalindrome_DP('babad'), ('bab', 'aba'))
        self.assertEqual(longestPalindrome_DP('abcdzdcab'), 'cdzdc')
        self.assertIn(longestPalindrome_Manacher('babad'), ('bab', 'aba'))
        self.assertEqual(longestPalindrome_Manacher('abcdzdcab'), 'cdzdc')



if __name__ == '__main__':
    unittest.main()

