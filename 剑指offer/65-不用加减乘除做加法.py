# -*- coding:utf-8 -*-
'''
    不用加减乘除做加法
=======================
写一个函数，求两个整数之和，要求在函数体内不得使用＋、－、×、÷四则运算符号。
'''

def add(num1, num2):
    '''
    思路：加法可以拆分成三个步骤，第一步是无进位加法，只坐各位相加不进位，进位
    舍去，如5+17=12；第二步做进位，如5+17的进位是10；第三步将前两步的结果相
    加起来得到最终结果12+10=22。二进制同理，但题目要求不能使用四则运算符号，
    因此每一步都需要用起来方法来实现，第一步可以用异或逻辑运算实现，第二步可以
    先求与运算再右移一位，第三步的加法可以利用前两步的方法进行运算，知道进位为
    0为止。
    '''
    if not isinstance(num1, int) or not isinstance(num2, int):
        return

    while num2 != 0:
        sum_ = (num1 ^ num2) & 0xFFFFFFFF
        carry = ((num1 & num2) << 1) & 0xFFFFFFFF
        num1 = sum_
        num2 = carry
    return num1 if num1 <= 0x7FFFFFFF else ~(num1 ^ 0xFFFFFFFF)


import unittest

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(111, 899), 1010)
        self.assertEqual(add(-1, 2), 1)
        self.assertEqual(add(1, -2), -1)
        self.assertEqual(add(3, 0), 3)
        self.assertEqual(add(0, -4), -4)
        self.assertEqual(add(-2, -8), -10)


if __name__ == '__main__':
    unittest.main()