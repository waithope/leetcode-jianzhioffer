# -*- coding:utf-8 -*-
'''
    第一个只出现一次的字符
===========================
在字符串中找出第一个只出现一次的字符。如输入"abaccdeff"，则输出"b"。
'''

def firstNotRepeatingChar(s):
    if not isinstance(s, str) or len(s) == 0:
        return

    charTable = {}
    for i in range(len(s)):
        if s[i] not in charTable:
            charTable[s[i]] = 1
        else:
            charTable[s[i]] += 1

    for i in range(len(s)):
        if charTable[s[i]] == 1:
            return s[i]
    return None

import unittest

class TestFirstNotRepeatingChar(unittest.TestCase):
    def test_first_not_repeating_char(self):
        self.assertEqual(firstNotRepeatingChar('google'), 'l')
        self.assertEqual(firstNotRepeatingChar('aabccdbd'), None)
        self.assertEqual(firstNotRepeatingChar('abcdefg'), 'a')
        self.assertEqual(firstNotRepeatingChar(None), None)


if __name__ == '__main__':
    unittest.main()