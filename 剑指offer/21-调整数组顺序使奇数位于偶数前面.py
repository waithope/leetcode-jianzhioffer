# -*- coding:utf-8 -*-
'''
    调整数组顺序使奇数位于偶数前面
==================================
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于
数组的前半部分，所有偶数位于数组的后半部分。
'''

def reorder(nums):
    '''
    提示：用两个指针，一个指针pLeft指向已调整好顺序的奇数位置，一个指针p从左到有
    遍历数组，如果遇到偶数，则判断当前指针p是否于pLeft相等，如果不相等，指针pLeft
    向后移动一个位置，随后与交换指针p指向的内交换。
    注：该类题目要注意程序的可扩展性，将判断条件以函数的形式给出。
    '''
    def isEven(n):
        return (n & 1) == 1

    def reorder(nums, func):
        small = -1
        for i in range(len(nums)):
            if func(nums[i]):
                small += 1
                if small != i:
                    nums[small], nums[i] = nums[i], nums[small]
        return nums

    if not isinstance(nums, list) or len(nums) <= 0:
        return
    return reorder(nums, isEven)


if __name__ == '__main__':
    print('Test1: ', reorder([]))
    print('Test2: ', reorder([1]))
    print('Test3: ', reorder([2,1]))
    print('Test4: ', reorder([1,2,3,4,5,6,7]))
    print('Test5: ', reorder([2,4,6,1,3,5,7]))
    print('Test6: ', reorder([1,3,5,7,2,4,6]))