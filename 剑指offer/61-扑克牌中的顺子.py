# -*- coding:utf-8 -*-
'''
        扑克牌中的顺子
============================
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王可以看成任意数字。
'''

def isContinuous(nums):
    '''
    思路：判断5张牌是否连续，就是判断按照牌的大小排序后的5张牌每张牌之间的
    间隔是否是等于0（如，4和5之间间隔为0），由于大小王可以看成任意数字，
    因此可以弥补一个间隔，当5张排序后的牌间隔为0，则说明这副牌是一个顺子。
    另外，当5张牌中出现对子，是不可能为顺子的，可直接返回False
    '''
    if not isinstance(nums, list) or len(nums) == 0:
        return False

    nums = sorted(nums)
    small = 0
    for num in nums:
        if num == 0:
            small += 1
        else: break
    big = small + 1
    gaps, zeros = 0, small
    while big < len(nums):
        if nums[big] == nums[small]:
            return False

        gaps += nums[big] - nums[small] - 1
        small = big
        big += 1
    return gaps <= zeros


import unittest

class TestIsContinuous(unittest.TestCase):
    def test_is_continuous(self):
        self.assertEqual(isContinuous(None), False)
        self.assertEqual(isContinuous([1,3,2,5,4]), True)
        self.assertEqual(isContinuous([1,3,2,6,4]), False)
        self.assertEqual(isContinuous([0,3,2,6,4]), True)
        self.assertEqual(isContinuous([0,3,1,6,4]), False)
        self.assertEqual(isContinuous([1,3,0,5,0]), True)
        self.assertEqual(isContinuous([1,3,0,7,0]), False)
        self.assertEqual(isContinuous([1,0,0,1,0]), False)


if __name__ == '__main__':
    unittest.main()