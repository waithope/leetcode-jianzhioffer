# -*- coding:utf-8 -*-
'''
        左旋转字符串
============================
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数
实现字符串左旋转操作的功能。比如输入字符串"abcdefg"和数字2，该函数将返回
左旋转2位得到的结果"cdefgab"。
'''

def leftRotateString(string, n):
    '''
    思路：以"abcdefg"为例，在第n=2个位置将字符串分割成两部分，分别是"ab"和
    "cdefg"，接着分别对这两个子字符串进行翻转得到"ba"和"gfedc"，最后将这两
    个字符串拼接起来再进行一次翻转就可以得到左翻转n个字符的结果字符串。
    '''
    def reverse(string, begin, end):
        while begin < end:
            string[begin], string[end] = string[end], string[begin]
            begin += 1
            end -= 1

    if (not isinstance(string, str) or len(string) == 0
        or not isinstance(n, int) or n < 1 or n >= len(string)):
        return string

    chars = list(string)
    reverse(chars, 0, n-1)
    reverse(chars, n, len(chars) - 1)

    reverse(chars, 0, len(chars) - 1)
    return ''.join(chars)


import unittest

class TestLeftRotateString(unittest.TestCase):
    def test_left_rotate_string(self):
        self.assertEqual(leftRotateString('abcdefg', 2), 'cdefgab')
        self.assertEqual(leftRotateString('abcdefg', 1), 'bcdefga')
        self.assertEqual(leftRotateString('abcdefg', 6), 'gabcdef')
        self.assertEqual(leftRotateString(None, 6), None)
        self.assertEqual(leftRotateString('abcdefg', 0), 'abcdefg')
        self.assertEqual(leftRotateString('abcdefg', 7), 'abcdefg')


if __name__ == '__main__':
    unittest.main()