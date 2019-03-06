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
    '''
    将中间结果进行保存，避免重复计算
    时间：O(n)
    '''
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

def fibonacci_matrix(n):
    '''
    用矩阵乘法求解fibonacci数列，时间复杂度可以提升到o(logn)
    时间：o(logn)
    '''
    def multiply(F, M):
        '''
        用对应元素相乘方法模拟矩阵乘法
        '''
        x = F[0][0] * M[0][0] + F[0][1] * M[1][0]
        y = F[0][0] * M[0][1] + F[0][1] * M[1][1]
        z = F[1][0] * M[0][0] + F[1][1] * M[1][0]
        k = F[1][0] * M[0][1] + F[1][1] * M[1][1]

        F[0][0], F[0][1], F[1][0], F[1][1] = x, y, z, k

    def power(F, n):
        if n == 0 or n == 1:
            return
        M = [[1, 1], [1, 0]]
        power(F, n // 2)
        multiply(F, F)
        if n % 2 != 0:
            multiply(F, M)

    if not isinstance(n, int):
        return
    if n == 0:
        return 0
    F = [[1, 1], [1, 0]]
    power(F, n-1)
    return F[0][0]

import unittest

class Test_Fibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(38), 39088169)
        self.assertEqual(fibonacci_matrix(100), 354224848179261915075)

if __name__ == '__main__':
    unittest.main()

