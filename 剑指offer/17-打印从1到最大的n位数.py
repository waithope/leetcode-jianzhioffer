# -*- coding:utf-8 -*-
'''
    打印从1到最大的n位数
==========================
输入数字n，按顺序打印从1到最大的n位十进制数。比如输入3，则打印出1、2、3
一直到最大的3位数999
'''

def print1ToMaxOfNDigits(n):
    '''
    提示：由于没有规定n的范围，当输入的n非常大的时候，可能会出现溢出的情况，
    也就是说我们要考虑大数问题。
    '''
    def incrementBy1(nums):
        isOverflow = False
        carry = 1
        for i in range(len(nums)-1, -1, -1):
            res = nums[i] + carry
            carry = res // 10
            nums[i] = res % 10
            if i == 0 and carry:
                isOverflow = True
        return isOverflow

    def printNumber(nums):
        isBeginningZero = True
        res = ''
        for i in range(len(nums)):
            if nums[i] != 0 and isBeginningZero:
                isBeginningZero = False
            if not isBeginningZero:
                res += str(nums[i])
        if res:
            print(res)

    if not isinstance(n, int) or n <= 0:
        return

    nums = [0] * n
    while not incrementBy1(nums):
        printNumber(nums)

def print1ToMaxOfNDigits_Recursively(n):
    '''
    提示：把n位数看成是一个全排列问题，每一位的数值范围都是从0~9递增，用递归可使代码更简洁
    '''
    def printNumber(nums):
        isBeginningZero = True
        res = ''
        for i in range(len(nums)):
            if nums[i] != 0 and isBeginningZero:
                isBeginningZero = False
            if not isBeginningZero:
                res += str(nums[i])
        if res:
            print(res)

    def digitsPermutation(nums, index):
        if index == len(nums):
            printNumber(nums)
            return

        for i in range(10):
            nums[index] = i
            digitsPermutation(nums, index+1)

    if not isinstance(n, int) or n <= 0:
        return

    nums = [0] * n
    digitsPermutation(nums, 0)



if __name__ == '__main__':
    # testing for normal version
    print1ToMaxOfNDigits(0)
    print1ToMaxOfNDigits(1)
    print1ToMaxOfNDigits(2)

    # testing for recursive version
    print1ToMaxOfNDigits_Recursively(0)
    print1ToMaxOfNDigits_Recursively(1)
    print1ToMaxOfNDigits_Recursively(2)
