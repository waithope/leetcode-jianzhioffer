# -*- coding:utf-8 -*-
'''
    青蛙跳台阶
===================
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''

def jumpFloor(n):
    '''
    青蛙跳台阶实际上就是斐波那契数列，为什么呢？
    假设我们把n级台阶时的跳法看成n的函数，当n>2时，第一次跳一级台阶，后面剩下的
    n-1级台阶的跳法就为f(n-1)；如果第一次跳二级台阶，后面剩下的n-2级台阶的跳法
    为f(n-2)，所以n级台阶的跳法为f(n-1)+f(n-2), 这其实就是斐波那契数列公式
    '''
    if not isinstance(n, int) or n <= 0:
        return
    result = [1, 2]
    if n < 3:
        return result[n]

    fiboMinusOne = 2
    fiboMinusTwo = 1
    for i in range(3, n+1):
        fiboN = fiboMinusOne + fiboMinusTwo
        fiboMinusTwo = fiboMinusOne  # 注：先保存fiboMinusOne，再用fiboN覆盖
        fiboMinusOne = fiboN
    return fiboN


import unittest

class Test_Jump_Floor(unittest.TestCase):
    def test_jump_floor(self):
        self.assertEqual(jumpFloor(3), 3)
        self.assertEqual(jumpFloor(4), 5)
        self.assertEqual(jumpFloor(99), 354224848179261915075)

if __name__ == '__main__':
    unittest.main()