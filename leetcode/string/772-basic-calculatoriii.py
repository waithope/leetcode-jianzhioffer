'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses ) and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-2147483648, 2147483647].

Some examples:

"1 + 1" = 2
" 6-4 / 2 " = 4
"2*(5+5*2)/3+(6/2+8)" = 21
"(2+6* 3+5- (3*14/7+2)*5)+3"=-12
'''


def calculate(s: str):
    if not isinstance(s, str) or len(s) == 0:
        return 0

    s += '+0'
    num, preOp = 0, '+'
    callStack, stack = [], []
    for i in range(len(s)):
        if s[i].isdigit():
            num = num * 10 + int(s[i])
        elif s[i].isspace():
            continue
        elif s[i] == '(':
            callStack.append(stack)
            callStack.append(preOp)
            stack, preOp = [], '+'
        else:
            if preOp == '+':
                stack.append(num)
            elif preOp == '-':
                stack.append(-num)
            elif preOp == '*':
                stack.append(stack.pop() * num)
            elif preOp == '/':
                stack.append(int(stack.pop() / num))
            if s[i] == ')':
                num = sum(stack)
                preOp = callStack.pop()
                stack = callStack.pop()
            else:
                num = 0
                preOp = s[i]
    return sum(stack)


import unittest

class TestCalculate(unittest.TestCase):
    def test_calculate(self):
        # self.assertEqual(calculate('1 + 1'), 2)
        # self.assertEqual(calculate(' 6-4 / 2 '), 4)
        self.assertEqual(calculate(' (1 + (4 + 5)) '), 10)
        # self.assertEqual(calculate('2*(5+5*2)/3+(6/2+8)'), 21)
        # self.assertEqual(calculate('(2+6* 3+5- (3*14/7+2)*5)+3'), -12)


if __name__ == '__main__':
    unittest.main()