# -*- coding:utf-8 -*-
'''
    Basic Calculator
========================
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
'''

def calculate(s: str):
    num, preOp, stack = 0, '+', []
    for i in range(len(s)):
        if s[i].isdigit():
            num = num * 10 + int(s[i])
        if s[i] in '+-*/' or i == len(s) - 1:
            if preOp == '+':
                stack.append(num)
            elif preOp == '-':
                stack.append(-num)
            elif preOp == '*':
                stack.append(stack.pop() * num)
            else:
                stack.append(int(stack.pop() / num))
            num = 0
            preOp = s[i]
    return sum(stack)


import unittest

class TestCalculate(unittest.TestCase):
    def test_calculate(self):
        self.assertEqual(calculate('3+2*2'), 7)
        self.assertEqual(calculate(' 3/2 '), 1)
        self.assertEqual(calculate(' 3+5 / 2 '), 5)


if __name__ == '__main__':
    unittest.main()