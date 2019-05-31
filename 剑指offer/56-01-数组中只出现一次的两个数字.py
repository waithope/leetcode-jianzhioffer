# -*- coding:utf-8 -*-
'''
    数组中只出现一次的两个数字
===============================
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现
一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
'''

def findNumAppearOnce(nums):
    '''
    思路：对两个相同的数进行异或操作，结果为0，因此对数组中的数字逐个进行异或操作，
    最后的结果就是两个只出现一次的数字异或之后的值。做到这一步还不够，还不能找出
    这两个数字具体是哪一个。我们可以利用上一步得到的结果将数组分成两个子数组，每一个
    子数组只有一个数字是出现一次的，其余的数字都出现两次。然后分别对每个数组异或求值，
    最终就可以分别得到只出现一次的那个数字。由于两个只出现一次的数字异或之后所得的值
    的二进制位中必然有一位是1，原因是它们数值不相同，而这个1就可以区分这两个数字。把
    第一个为1的位置记作a，我们把数组中每个数字二进制位第a位为1的分到左数组，不为1的分
    到右数组，这一步保证了每个子数组其他数字都出现两次，原因是相同的两个数字必然只会
    分到其中一个数组当中。最后，分别对每个数组进行异或操作，得到最终的两个数字。
    '''
    def findFirstBitIs1(num):
        if not isinstance(num, int):
            return
        indexOfBit1 = 0
        while num != 0 and (num & 1) == 0:
            num >>= 1
            indexOfBit1 += 1
        return indexOfBit1

    if not isinstance(nums, list) or len(nums) == 0:
        return

    resultExOR = 0
    for num in nums:
        resultExOR ^= num

    indexOfBit1 = findFirstBitIs1(resultExOR)
    temp = 1 << indexOfBit1
    res1, res2 = 0, 0
    for num in nums:
        if num & temp:
            res1 ^= num
        else:
            res2 ^= num
    return res1, res2


import unittest

class TestFindNumAppearOnce(unittest.TestCase):
    def test_find_num_appear_once(self):
        self.assertEqual(findNumAppearOnce([2,4,3,6,3,2,5,5]), (6, 4))
        self.assertEqual(findNumAppearOnce([2,4,3,6,3,2,5,5]), (6, 4))
        self.assertEqual(findNumAppearOnce([4,6]), (6, 4))
        self.assertEqual(findNumAppearOnce([4,6,1,1,1,1]), (6, 4))


if __name__ == '__main__':
    unittest.main()




