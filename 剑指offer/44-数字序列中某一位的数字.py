# -*- coding:utf-8 -*-
'''
    数字序列中某一位的数字
===========================
数字以0123456789101112131415...的格式序列化到一个字符序列中。在这个序列中，第5位
（从0开始计数，0，1，2，3，4，5位）是5，第13位是1，第19位是4，等等。请写一个函数，
在不提供字符序列的情况下，求任意第n位对应的数字。
'''

def digitAtIndex(index):
    '''
    思路：观察序列和整数的规律，0~9是个位数，每一个整数占1个位置，10~99是两位数，
    每一个整数占2个位置，100~999是三位数，每一个整数占3个位置，依次类推。有了这个
    框架之后，我们只要定位index在哪一个区间就可以了。比如求第19位对应的数字，首先，
    初始化digit=1，digit表示在第几个区间，比如digit=2就表示第二个区间，该区间内
    的每一个整数占两个位置。接着计算第一个区间的总长度，10^(digit)=10，10*digit
    =10，表示第一个区间所有的10个整数总共占10个位置。由于19>10，说明19在后面的区间，
    所以接下来我们要在下一个区间找第9（19-10）位的数字。更新digit=digit+1=2，
    计算第二个区间的总长度，10^2=100，100-10=90（第二个区间的整数个数），
    90*digit=180，第二个区间所有的90个整数总共占180个位置。由于9<180，说明要找的
    数字在这个区间内，9通过对digit取整得4（9//2向下取整）定位到第二个区间第4个整数
    14，9通过对digit取余得1（9%2）定位到14的第“1”位4的数字（因为定位到14就是定位
    到1，由于余数为1，向右移动一位，就定为到4这个数字了。）
    '''
    if not isinstance(index, int) or index < 0:
        return -1

    start = 0
    digit = 1
    base = 10
    while True:
        gap = base ** digit - start
        numbers = gap * digit
        if index < numbers:
            divider = index // digit
            remainder = index % digit
            res = start + divider
            return int(str(res)[remainder])
        index -= numbers
        start = base ** digit
        digit += 1


import unittest

class TestDigitAtIndex(unittest.TestCase):
    def test_digit_at_index(self):
        self.assertEqual(digitAtIndex(0), 0)
        self.assertEqual(digitAtIndex(1), 1)
        self.assertEqual(digitAtIndex(9), 9)
        self.assertEqual(digitAtIndex(10), 1)
        self.assertEqual(digitAtIndex(189), 9)
        self.assertEqual(digitAtIndex(190), 1)
        self.assertEqual(digitAtIndex(1000), 3)
        self.assertEqual(digitAtIndex(1001), 7)
        self.assertEqual(digitAtIndex(1002), 0)


if __name__ == '__main__':
    unittest.main()