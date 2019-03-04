# -*- coding:utf-8 -*-
'''
    斐波那契数列
===================
例：[1, 1, 2, 3, 5, 8, 13, 21, 34, ....]
求斐波那契数列的第n项
写一个函数，输入n，求斐波那契（Fibonacci）数列的第n项，斐波那契数列定义如下：
fn = {
        0                   n = 0;
        1                   n = 1;
        f(n-1) + f(n-2)     n > 1
}
'''

def fibonacci(n):
    result = [0, 1]
    if n < 2:
        return result[n]

    fiboMinusOne = 1
    fiboMinusTwo = 0
    for i in range(2, n+1):
        fiboN = fiboMinusOne + fiboMinusTwo
        fiboMinusTwo = fiboMinusOne
        fiboMinusOne = fiboN
    return fiboN


import unittest

class Test_Fibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(38), 39088169)

if __name__ == '__main__':
    unittest.main()

