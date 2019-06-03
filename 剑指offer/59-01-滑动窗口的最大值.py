# -*- coding:utf-8 -*-
'''
        滑动窗口的最大值
==============================
给定一个数组和滑动窗口的大小，请找出所有滑动窗口里的最大值。例如，如果输入数组
{2, 3, 4, 2, 6, 2, 5, 1}及滑动窗口的大小3，那么一共存在6个滑动窗口，它们的
最大值分别为{4, 4, 6, 6, 6, 5}。
'''
from collections import deque
def maxInWindow(nums, size):
    '''
    思路：蛮力法就是扫描每个滑动窗口的所有数字并找出其中的最大值，该方法的时间复杂度
    为O(n*k)，k为窗口大小。比这个方法更优的解法是把滑动窗口看作是一个队列，但不是把
    所有数字的存入队列当中，而是将有可能成为窗口内最大值的数字存入队列当中。每当遇到
    一个数字时，将队列中小于该数字的数字都弹出，保证队列的头部为窗口内的最大值。以上
    操作完成之后，将该数字添加到队列尾部；如果队列头部的数字不在窗口中（因此要求队列
    保存的是数字在数组中的下标），则将其从左边弹出(popleft())。在每次处理一个数字
    的时候，要先将上一个窗口内的最大值，即队列头部的数字添加到结果列表中。
    '''
    if (not isinstance(nums, list) or not isinstance(size, int)
        or size < 1 or len(nums) < size):
        return []

    res = []
    indexDeque = deque()
    for i in range(size):
        while len(indexDeque) != 0 and nums[indexDeque[-1]] < nums[i]:
            indexDeque.pop()
        indexDeque.append(i)
    for i in range(size, len(nums)):
        res.append(nums[indexDeque[0]])
        while len(indexDeque) != 0 and nums[indexDeque[-1]] < nums[i]:
            indexDeque.pop()
        while len(indexDeque) != 0 and (i - indexDeque[0]) >= size:
            indexDeque.popleft()
        indexDeque.append(i)
    res.append(nums[indexDeque[0]])
    return res


import unittest

class TestMaxInWindow(unittest.TestCase):
    def test_max_in_window(self):
        self.assertEqual(maxInWindow([2,3,4,2,6,2,5,1], 3), [4,4,6,6,6,5])
        self.assertEqual(maxInWindow([1,3,-1,-3,5,3,6,7], 3), [3,3,5,5,6,7])
        self.assertEqual(maxInWindow([1,3,5,7,9,11,13,15], 4), [7,9,11,13,15])
        self.assertEqual(maxInWindow([16,14,12,10,8,6,4], 5), [16,14,12])
        self.assertEqual(maxInWindow([10,14,12,11], 1), [10,14,12,11])
        self.assertEqual(maxInWindow([10,14,12,11], 4), [14])
        self.assertEqual(maxInWindow([10,14,12,11], 0), [])
        self.assertEqual(maxInWindow([10,14,12,11], 5), [])
        self.assertEqual(maxInWindow([], 5), [])


if __name__ == '__main__':
    unittest.main()


