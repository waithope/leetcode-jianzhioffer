# -*- coding:utf-8 -*-
'''
    二进制中1的个数
======================
请实现一个函数，输入一个整数，输出该数二进制表示中1的个数。例如，把9表示成
二进制是1001，有2位是1。因此，如果输入9，则该函数输出2。
'''

def numberOf1(n):
    '''
    思路：通过把一个整数减去1得到的结果与原整数求与运算，把该整数二进制表示中
    最右边的1变成0，该整数二进制表示有多少个1，就循环重复多少次上述过程，直到
    整数最后变为0为止。
    '''
    if not isinstance(n, int):
        return 0

    count = 0
    while n:
        count += 1
        n &= n - 1
    return count


import unittest

class TestNumberOf1(unittest.TestCase):
    def test_number_of_1(self):
        self.assertEqual(numberOf1(0), 0)
        self.assertEqual(numberOf1(1), 1)
        self.assertEqual(numberOf1(10), 2)
        self.assertEqual(numberOf1(0x7FFFFFFF), 31)
        self.assertEqual(numberOf1(0xFFFFFFFF), 32)
        self.assertEqual(numberOf1(0x80000000), 1)

if __name__ == '__main__':
    unittest.main()
