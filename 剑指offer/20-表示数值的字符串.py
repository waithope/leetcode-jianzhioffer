# -*- coding:utf-8 -*-
'''
    表示数值的字符串
======================
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100"、
"5e2"、"-123"、"3.1416"及"-1E-16"都表示数值，但"12e"、"1a3.14"、"1.2.3"、
"+-5"及"12e+5.4"都不是。
'''

def isNumeric(s):
    '''
    数值的格式可以用如下形式表示：
    A[.B][e|EC]或.B[e|EC]，其中A和C为整数(可有正负号也可没有)，B为无符号整数
    '''
    def scanInteger(s, index):
        if index < len(s) and s[index] in ('+', '-'):
            index += 1
        return scanUnsignedInteger(s, index)
    def scanUnsignedInteger(s, index):
        old_index = index
        while index < len(s) and s[index] in '0123456789':
            index += 1
        return index != old_index, index

    if not isinstance(s, str) or len(s) <= 0:
        return False

    isSatisfy, index = scanInteger(s, 0)
    if index < len(s) and s[index] == '.':
        isFloat, index = scanUnsignedInteger(s, index + 1)
        isSatisfy = (isSatisfy or isFloat)

    if index < len(s) and s[index] in ('E', 'e'):
        isExp, index = scanInteger(s, index + 1)
        isSatisfy = isSatisfy and isExp
    return (isSatisfy and index == len(s))



import unittest

class TestIsNumeric(unittest.TestCase):
    def test_is_numeric(self):
        self.assertEqual(isNumeric('100'), True)
        self.assertEqual(isNumeric('123.45e+6'), True)
        self.assertEqual(isNumeric('+500'), True)
        self.assertEqual(isNumeric('5e2'), True)
        self.assertEqual(isNumeric('3.1416'), True)
        self.assertEqual(isNumeric('600.'), True)
        self.assertEqual(isNumeric('-.123'), True)
        self.assertEqual(isNumeric('-1E-16'), True)
        self.assertEqual(isNumeric('1.79769313486232E+308'), True)
        self.assertEqual(isNumeric('12e'), False)
        self.assertEqual(isNumeric('1a3.14'), False)
        self.assertEqual(isNumeric('1+23'), False)
        self.assertEqual(isNumeric('1.2.3'), False)
        self.assertEqual(isNumeric('+-5'), False)
        self.assertEqual(isNumeric('1.2.3'), False)


if __name__ == '__main__':
    unittest.main()
