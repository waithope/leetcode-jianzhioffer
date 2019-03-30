# -*- coding:utf-8 -*-
'''
    正则表达式匹配
=====================
请实现一个函数用来匹配包含'.'和'*'的正则表达式。模式中的字符'.'表示任意一个
字符，而'*'表示它前面的字符可以出现任意次(含0次)。匹配是指字符串中的所有字符
匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和
"ab*a"均不匹配。
'''

def match(s, pattern):
    '''
    提示：这里需要注意，在进行匹配的过程中，模式字符串当前匹配字符的下一个
    字符是"*"的时候，需要考虑三种情况， 第一种字符串向后移动一个字符，模式
    字符串不移动；第二种字符串向后移动一个字符，模式字符串向后移动两个字符；
    第三种字符串不移动，模式字符串向后移动2个字符。
    '''
    def matchCore(s, pattern):
        if len(s) == len(pattern) == 0:
            return True
        if len(pattern) == 0 and len(s) != 0:
            return False
        if len(s) == 0 and len(pattern) != 0:
            if len(pattern) > 1 and pattern[1] == '*':
                return matchCore(s, pattern[2:])
            else:
                return False
        else:
            if len(pattern) > 1 and pattern[1] == '*':
                if s[0] != pattern[0] and pattern[0] != '.':
                    return matchCore(s, pattern[2:])
                else:
                    return (matchCore(s[1:], pattern)
                            or matchCore(s[1:], pattern[2:])
                            or matchCore(s, pattern[2:]))
            else:
                if s[0] == pattern[0] or pattern[0] == '.':
                    return matchCore(s[1:], pattern[1:])
                else:
                    return False

    if not isinstance(s, str) or not isinstance(pattern, str):
        return False

    return matchCore(s, pattern)


import unittest

class TestMatch(unittest.TestCase):
    def test_match(self):
        self.assertEqual(match('', ''), True)
        self.assertEqual(match('', '.*'), True)
        self.assertEqual(match('', '.'), False)
        self.assertEqual(match('', 'c*'), True)
        self.assertEqual(match('aab', 'c*a*b'), True)
        self.assertEqual(match('bbbba', '.*a*a'), True)
        self.assertEqual(match('bcbbabab', '.*a*a'), False)


if __name__ == '__main__':
    unittest.main()