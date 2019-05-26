# -*- coding:utf-8 -*-
'''
        丑数
=======================
我们把只包含因子2、3和5的数称作丑数（Ugly Number）。求按从小到大的顺序的第1500个
丑数。例如6、8都是丑数，但14不是，因为它包含因子7。习惯上我们把1当做第一个丑数。
'''

def getUglyNum(index):
    '''
    通过一个个去判断数字去找到目标丑数的方式存在时间效率的问题，下面通过空间换时间的
    思路提供一个时间效率优于之前方法的解法。
    思路：下一个丑数是当前丑数中的某一个丑数乘以2、3或者5的结果，记当前丑数中的最大
    丑数为M，将当前丑数分别乘以2、3、5，并将第一个大于M的结果记录为M2、M3和M5，再
    M2、M3和M5中最小的那一个丑数就是下一个我们要的丑数。然而，这种方式还不是最好的，
    因为它需要将当前每一个丑数都乘以2、3、5因子。我们只要每次更新记录那个乘以2、3、5
    因子之后大于最大丑数的那个丑数的下标，在下一次丑数的计算中，直接取这个下标对应的
    丑数，直接乘以对应的因子就可以了。
    '''
    if not isinstance(index, int) or index <= 0:
        return 0

    uglyNums = [0] * index
    uglyNums[0] = 1
    indexMultiply2 = 0
    indexMultiply3 = 0
    indexMultiply5 = 0
    nextIndex = 1

    while nextIndex < index:
        uglyNums[nextIndex] = min(uglyNums[indexMultiply2] * 2,
                                  uglyNums[indexMultiply3] * 3,
                                  uglyNums[indexMultiply5] * 5)

        while uglyNums[indexMultiply2]*2 <= uglyNums[nextIndex]:
            indexMultiply2 += 1
        while uglyNums[indexMultiply3]*3 <= uglyNums[nextIndex]:
            indexMultiply3 += 1
        while uglyNums[indexMultiply5]*5 <= uglyNums[nextIndex]:
            indexMultiply5 += 1

        nextIndex += 1

    return uglyNums[nextIndex - 1]


import unittest

class TestGetUglyNums(unittest.TestCase):
    def test_get_ugly_nums(self):
        self.assertEqual(getUglyNum(1), 1)
        self.assertEqual(getUglyNum(2), 2)
        self.assertEqual(getUglyNum(5), 5)
        self.assertEqual(getUglyNum(7), 8)
        self.assertEqual(getUglyNum(11), 15)
        self.assertEqual(getUglyNum(1500), 859963392)


if __name__ == '__main__':
    unittest.main()
