# -*- coding:utf-8 -*-
'''
    1-n整数中1出现的次数
===========================
输入一个整数n，求1-n这n个整数的十进制表示中1出现的次数。例如，输入12，1-12这些
整数中包含1的数字有1、10、11和12，1一共出现5次。
'''


def numberOf1Between1AndN(n):
    '''
    参考博客：https://blog.csdn.net/yi_Afly/article/details/52012593
    解题思路：把整数n看成两部分，rounds(轮次)和weight，weight是十进制中的
    0~9，weight从0加到9为一个轮次，再加1又会回到0进行第二个轮次。假设n=514,
    在循环开始前设置rounds=514，base=1(base，一个轮次1出现的次数)，先从最
    低位个位开始，weight=rounds%10=4，rounds=rounds//10=51，说明0~9这种
    周期有51轮，weight>1，说明1又出现一次，所以个位1出现的总次数为51+1=52；
    接着分析十位，rounds=51，base=10*base=10（十位可表示的范围是0~99，各个
    数字在十位出现的次数都为10，10，11，12，13，14，15，16，17，18，19），
    weight=rounds%10=1，rounds=rounds//10=5，说明在十位0~9这种周期有5轮，
    weight=1，当weight=1时，在十位上剩余次数为该位的前一位的数加上1（514%base+1
    =5，10，11，12，13，14），所以十位1出现的总次数位5*10+5=55；然后分析百位，
    rounds=5，base=10*base=100（百位克表示的范围是0~999，各个数字在百位出现
    的次数为100），weight=rounds%10=5，rounds=rounds//10=0，由于weight=5>1,
    说明在百位0~9这种周期进行了一半左右，由于覆盖完了1，所有在百位1出现的次数位1*100；
    由于此时rounds=0，循环结束，将各个位置上的次数相加就是最后的总次数，
    52+55+100=207
    '''
    if not isinstance(n, int) or n < 1:
        return 0

    count, base, rounds = 0, 1, n
    while rounds > 0:
        weight = rounds % 10
        rounds //= 10
        count += base * rounds
        if weight == 1:
            count += (n % base) + 1
        elif weight > 1:
            count += base
        base *= 10
    return count


import unittest

class TestNumberOf1Between1AndN(unittest.TestCase):
    def test_number_of_1(self):
        self.assertEqual(numberOf1Between1AndN(0), 0)
        self.assertEqual(numberOf1Between1AndN(1), 1)
        self.assertEqual(numberOf1Between1AndN(5), 1)
        self.assertEqual(numberOf1Between1AndN(10), 2)
        self.assertEqual(numberOf1Between1AndN(12), 5)
        self.assertEqual(numberOf1Between1AndN(55), 16)
        self.assertEqual(numberOf1Between1AndN(99), 20)
        self.assertEqual(numberOf1Between1AndN(504), 201)
        self.assertEqual(numberOf1Between1AndN(514), 207)
        self.assertEqual(numberOf1Between1AndN(524), 213)
        self.assertEqual(numberOf1Between1AndN(10000), 4001)
        self.assertEqual(numberOf1Between1AndN(21345), 18821)


if __name__ == '__main__':
    unittest.main()