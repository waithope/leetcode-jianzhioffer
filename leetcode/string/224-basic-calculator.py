# -*- coding:utf-8 -*-
'''
    Basic Calculator
========================
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
'''

def calculate(s: str):
    num, result, sign = 0, 0, 1
    stack = []
    for i in range(len(s)):
        if s[i].isdigit():
            num = num * 10 + (ord(s[i]) - ord('0'))
        elif s[i] == '+':
            result += sign * num
            num = 0
            sign = 1
        elif s[i] == '-':
            result += sign * num
            num = 0
            sign = -1
        elif s[i] == '(':
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif s[i] == ')':
            result += sign * num
            num = 0
            result *= stack.pop()
            result += stack.pop()
    #如果字符串中没有运算符只有数字的时候，result没有进行累加，所以需要在这一步判断
    if num != 0:
        result += sign * num
    return result