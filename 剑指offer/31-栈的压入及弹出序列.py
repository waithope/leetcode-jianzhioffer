# -*- coding:utf-8 -*-
'''
    栈的压入、弹出序列
========================
输入两个整数序列，第一个序列表示栈的压入顺序（注：压入期间有弹出），请判断
第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如，序列
{1,2,3,4,5}是某栈的压栈序列，序列{4,5,3,2,1}是该压栈序列对应的一个弹出
序列，但{4,3,5,1,2}就不可能是该压栈序列的弹出序列。
'''

def isPopOrder(pushList, popList):
    '''
    思路：创建一个辅助栈，根据压入序列pushList和弹出序列popList模拟整数的
    压栈以及出栈过程。
    具体流程：变量nextPush记录在压栈序列中将要压入辅助栈的元素的位置，初始值为0；
    变量nextPop记录在弹出序列中将要弹出的元素的位置，初始位置为0。当辅助栈为空时，
    压入元素pushList[nextPush]；当辅助栈不为空，且辅助栈栈顶元素不等于
    popList[nextPop]，将pushList[nextPush++]元素陆续压入辅助栈，直到辅助栈
    栈顶元素等于popList[nextPop]为止。当辅助栈栈顶元素等于popList[nextPop]时，
    辅助栈弹出栈顶元素，并将nextPop指向弹出序列的下一个位置。最后，如果nextPop==
    弹出序列长度，则表明弹出序列是压栈序列的弹出顺序，否则，不是。
    '''
    if not isinstance(pushList, list) or not isinstance(popList, list):
        return False
    if len(pushList) == 0 or len(popList) == 0 or len(pushList) != len(popList):
        return False

    isPossible = False
    auxStack = []
    nextPush, nextPop = 0, 0
    while nextPop < len(popList):
        while auxStack == [] or (auxStack[-1] != popList[nextPop]):
            if nextPush == len(pushList):
                break
            auxStack.append(pushList[nextPush])
            nextPush += 1

        if auxStack[-1] != popList[nextPop]:
            break
        auxStack.pop()
        nextPop += 1

    if nextPop == len(popList):
        isPossible = True
    return isPossible


import unittest

class TestIsPopOrder(unittest.TestCase):
    def test_is_pop_order(self):
        self.assertEqual(isPopOrder([1,2,3,4,5], [4,5,3,2,1]), True)
        self.assertEqual(isPopOrder([1,2,3,4,5], [3,5,4,2,1]), True)
        self.assertEqual(isPopOrder([1,2,3,4,5], [4,3,5,1,2]), False)
        self.assertEqual(isPopOrder([1,2,3,4,5], [3,5,4,1,2]), False)
        self.assertEqual(isPopOrder([1], [2]), False)
        self.assertEqual(isPopOrder([1], [1]), True)
        self.assertEqual(isPopOrder(None, None), False)


if __name__ == '__main__':
    unittest.main()