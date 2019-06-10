# -*- coding:utf-8 -*-
'''
    把字符串转换为整数
=========================
请你写一个函数StrToInt，实现把字符串转换成整数这个功能。当然，不能使用atoi或者
其他类似的库函数。
'''

def strToInt(s):
    '''
    思路：从字符串的左边向右边逐个读取，以十进制进行计算。这里需要注意的点主要是
    一些非法输入和特殊符号，比如空字符串、空指针、正负号以及字符串中不属于0~9的字符
    等。
    '''
    def strToIntCore(listOfChars, minus=False):
        if len(listOfChars) == 0:
            return None
        num, sign = 0, 0
        sign = -1 if minus else 1
        for char in listOfChars:
            if char >= '0' and char <= '9':
                num = num * 10 + sign * (ord(char) - ord('0'))
            else:
                num = None
                break
        return num

    if not isinstance(s, str) or len(s) == 0:
        return None

    minus, num = False, 0
    listOfChars = list(s)
    if listOfChars[0] == '-':
        minus = True
        num = strToIntCore(listOfChars[1:], minus)
    elif listOfChars[0] == '+':
        num = strToIntCore(listOfChars[1:], minus)
    else:
        num = strToIntCore(listOfChars, minus)

    return num


import unittest

class TestStrToInt(unittest.TestCase):
    def test_str_to_int(self):
        self.assertEqual(strToInt(None), None)
        self.assertEqual(strToInt(''), None)
        self.assertEqual(strToInt('+'), None)
        self.assertEqual(strToInt('-'), None)
        self.assertEqual(strToInt('123'), 123)
        self.assertEqual(strToInt('+123'), 123)
        self.assertEqual(strToInt('-123'), -123)
        self.assertEqual(strToInt('1a33'), None)
        self.assertEqual(strToInt('+0'), 0)
        self.assertEqual(strToInt('-0'), 0)
        self.assertEqual(strToInt('+2147483647'), 2147483647)
        self.assertEqual(strToInt('-2147483647'), -2147483647)


if __name__ == '__main__':
    unittest.main()




