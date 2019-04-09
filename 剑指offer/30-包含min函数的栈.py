# -*- coding:utf-8 -*-
'''
    包含min函数的栈
======================
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的min函数。
在该栈中，调用min、push及pop的时间复杂度都是O(1)。
'''

class StackWithMin(object):
    '''
    思路：直线思维是在进行压栈的时候，用一个变量保存当前的最小值，但是这个
    方法有一个问题，就是当最小值被pop出去时，剩下元素的最小值或者说次小值就不知道了。
    一个好的方法是创建一个辅助栈，当栈push的同时，将当前最小值push到辅助栈，当
    栈pop的同时，辅助栈也同步pop，这样一来，辅助栈的栈顶元素就一直是最小元素。
    '''
    def __init__(self):
        self.realStack = []
        self.minStack = []
    def push(self, val):
        assert isinstance(val, (int, float))

        self.realStack.append(val)
        if len(self.minStack) == 0:
            self.minStack.append(val)
        elif val < self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])
    def pop(self):
        assert(len(self.realStack) > 0 and len(self.minStack) > 0)
        self.minStack.pop()
        return self.realStack.pop()
    def min(self):
        assert(len(self.realStack) > 0 and len(self.minStack) > 0)
        return self.minStack[-1]



def test(testname, stack, expected):
    if testname:
        print('{} begins: '.format(testname))
    if stack.min() == expected:
        print('Passed.')
    else:
        print('Failed')


if __name__ == '__main__':
    stack = StackWithMin()

    stack.push(3)
    test('Test1', stack, 3)

    stack.push(4)
    test('Test2', stack, 3)

    stack.push(2)
    test('Test3', stack, 2)

    stack.push(3)
    test('Test4', stack, 2)

    stack.pop()
    test('Test5', stack, 2)

    stack.pop()
    test('Test6', stack, 3)

    stack.pop()
    test('Test7', stack, 3)

    stack.push(0)
    test('Test8', stack, 0)


