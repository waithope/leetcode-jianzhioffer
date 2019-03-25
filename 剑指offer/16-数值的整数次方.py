# -*- coding:utf-8 -*-
'''
    数值的整数次方
======================
实现函数double Power(double base, int exponent), 求base的exponent次方。不得
使用库函数，同时不需要考虑大数问题。
'''


def Power(base, exponent):
    '''
    提示：需要注意输入的指数(exponent)小于1的情况，也就是exponent为零、负数情况
    '''
    def powerWithUnsignedExponent(base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base

        res = powerWithUnsignedExponent(base, exponent >> 1)
        res *= res
        if (exponent & 1) == 1:
            res *= base
        return res

    if not isinstance(exponent, int) or not isinstance:
        raise TypeError('Inapropriate argument type')

    try:
        res = powerWithUnsignedExponent(base, abs(exponent))
        if exponent < 0:
            res = 1 / res
    except ZeroDivisionError:
        print('Error: base is zero')
    else:
        return res


import unittest

class TestPower(unittest.TestCase):
    def test_power(self):
        self.assertEqual(Power(2, 3), 8)
        self.assertEqual(Power(-2, 3), -8)
        self.assertEqual(Power(2, -3), 0.125)
        self.assertEqual(Power(2, 0), 1)
        self.assertEqual(Power(0, 0), 1)
        self.assertEqual(Power(0, 4), 0)
        self.assertEqual(Power(0, -4), None)


if __name__ == '__main__':
    unittest.main()
