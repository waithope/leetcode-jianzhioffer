# -*- coding:utf-8 -*-
'''
    数组中唯一只出现一次的数字
===============================
在一个数组中除了一个数字只出现一次之外，其他数字都出现了三次。
请找出那个只出现一次的数字。
'''

def findNumAppearOnce(nums):
    '''
    思路：将每个数字以二进制的形式看待，对于同时出现三次的某个数字来说，将这三个
    数字的二进制表示的每一位分别求和，每一位的和都能被3整除。因此，对所有数字的
    二进制表示的每一位分别求和，如果某一位能够被3整除，说明那个只出现一次的数字在
    这一位是0；否则就是1。最终，我们就可以得到只出现一次的数字的二进制表示，再将
    它转换为十进制表示即可返回。

    注：python中整数的表示是无限精度的，因此，程序末尾通过移位计算整数的方法目前
    还没有找到很好解决负数的情况。
    '''
    if not isinstance(nums, list) or len(nums) == 0:
        return

    maxBitLen = max([len(bin(num))-2 for num in nums])
    bitSum = [0] * maxBitLen
    for num in nums:
        bitMask = 1
        for i in range(maxBitLen - 1, -1, -1):
            if (bitMask & num) != 0:
                bitSum[i] += 1
            bitMask <<= 1
    print(bitSum)
    result = 0
    for bit in bitSum:
        result <<= 1
        result += (bit % 3)

    return result

import unittest

class TestFindNumAppearOnce(unittest.TestCase):
    def test_find_num_appear_once(self):
        self.assertEqual(findNumAppearOnce([1,1,2,2,2,1,3]), 3)
        self.assertEqual(findNumAppearOnce([4,3,3,2,2,2,3]), 4)
        self.assertEqual(findNumAppearOnce([4,4,1,1,1,7,4]), 7)
        self.assertEqual(findNumAppearOnce([0,3467,0,0,0,0,0,0]), 3467)
        self.assertEqual(findNumAppearOnce([-10,214,214,214]), -10)
        self.assertEqual(findNumAppearOnce([-209,3467,-209,-209]), 3467)
        self.assertEqual(findNumAppearOnce([1024, -1025, 1024, -1025,
                                            1024, -1025, 1023]), 1023)
        self.assertEqual(findNumAppearOnce([-1024, -1024, -1024, -1023]), -1023)


if __name__ == '__main__':
    unittest.main()

