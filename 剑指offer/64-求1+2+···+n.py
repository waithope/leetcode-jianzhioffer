# -*- coding:utf-8 -*-
'''
        求1+2+···+n
=============================
求1+2+…+n，要求不能使用乘除法、for、while、if、else、switch、case
等关键字及条件判断语句（A?B:C）。
'''

def sum1ToN(n):
    '''
    思路：要求不能使用乘除法，也不能使用循环语句，但可以使用加法。通过
    递归的方式可以实现循环加法。
    '''
    return n and sum1ToN(n - 1) + n


import unittest

class TestSum1ToN(unittest.TestCase):
    def test_sum_1_to_n(self):
        self.assertEqual(sum1ToN(0), 0)
        self.assertEqual(sum1ToN(1), 1)
        self.assertEqual(sum1ToN(5), 15)
        self.assertEqual(sum1ToN(10), 55)
        self.assertEqual(sum1ToN(100), 5050)


if __name__ == '__main__':
    unittest.main()


