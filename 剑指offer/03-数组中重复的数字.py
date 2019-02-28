# -*- coding:utf-8 -*-
'''
    数组中重复的数字
======================
找出数组中重复的数字。
在一个长度为n的数组里的所有数字都在0~n-1的范围内。数组中某些数字是重复的，
但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个
重复的数字。例如，如果输入长度为7的数组{2, 3, 1, 0, 2, 5, 3}，那么对应
的输出是重复的数字2或3。
'''

def duplicate1(numbers):
    '''
    修改原数组列表，时间O(n), 空间O(1)
    '''
    if numbers is None or len(numbers) <= 0:
        return False, None
    for num in numbers:
        if num < 0 or num >= len(numbers):
            return False, None
    for i in range(len(numbers)):
        while numbers[i] != i:
            if numbers[i] == numbers[numbers[i]]:
                return True, numbers[i]
            else:
                # python赋值表达式计算顺序先等式右边，后左边，
                # 如果直接交换number[i], numbers[number[i]]程序结果不能达到预期
                index = numbers[i]
                numbers[i], numbers[index] = numbers[index], numbers[i]
    return False, None

'''
    数组中重复的数字
======================
找出数组中重复的数字。
在一个长度为n+1的数组里的所有数字都在1~n的范围内。所以数组中至少有一个数字
是重复的。请找出数组中任意一个重复的数字。例如，如果输入长度为8的数组
{2, 3, 5, 4, 3, 2, 6, 7}，那么对应的输出是重复的数字2或3。
'''

def duplicate2(numbers):
    '''
    不修改原数组，时间O(nlgn)，空间O(1)
    '''
    def count_range(numbers, low, high):
        count = 0
        for num in numbers:
            if num >= low and num <= high:
                count += 1
        return count

    if len(numbers) <= 0:
        return False, None
    for num in numbers:
        if num < 1 and num > len(numbers) - 1:
            return False, None

    start, end = 1, len(numbers) - 1
    while start <= end:
        mid = start + (end - start) // 2
        count = count_range(numbers, start, mid)
        if start == end:
            if count > 1:
                return True, start
        if count <= mid - start + 1:
            start = mid + 1
        else:
            end = mid - 1
    return False, None




import unittest

class TestDuplicate(unittest.TestCase):
    def test_duplicate(self):
        self.assertEqual(duplicate1([2,3,1,0,2,5,3]), (True, 2))
        self.assertEqual(duplicate2([2,3,5,4,3,2,6,7]), (True, 3))

if __name__ == '__main__':
    unittest.main()


