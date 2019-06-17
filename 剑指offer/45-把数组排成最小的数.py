# -*- coding:utf-8 -*-
'''
    把数组排成最小的数
========================
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中
最小的一个。例如输入数组{3, 32, 321}，则打印出这3个数字能排成的最小数字321323。
'''

from functools import cmp_to_key
def printMinNumber(nums):
    '''
    思路：将问题看成是一个排序问题，重新定义一个新的排序规则，在新的排序规则中
    如果a<b，就表示a和b拼接起来的整数ab要小于b和a拼接起来的整数ba，最后对整个
    数组进行排序，并将排序结果进行从左到右拼接得到最小数字。

    为什么这种排序规则是有效的，可以用分情况讨论的思路证明这个规则。对于数组中的
    a,b来说，排出的数字要么a在b前面，要么b在a前面。假设其他元素已经排成一个
    最小值XXX。有以下三种情况:
　　 1. abXXX
　　     显然如果ab<ba，abXXX<baXXX
　　 2. XXXab
　　　   显然如果ab<ba，abXXX<baXXX
　　 3. aXXXb
　　　   我们将中间部分看成c,则有acb.如果ab<ba已知,需证明acb<bca。假设a,c,b的位数
        分别是m,n,l（个/十/百），若acb>bca，则a*10^m+c*10^n+b>b*10^l+c*10^n+a，
        两边同时减c*10^n，可以得到a*10^m+b>b*10^l+a 即ab>ba和已知矛盾。由此可证acb<bca
    '''

    def compare(a, b):
        if not isinstance(a, str) or not isinstance(b, str):
            raise ValueError('Parameter Is Not String Type')

        ab = a + b
        ba = b + a
        if ab < ba:        #为了防止大数溢出，采用字符串比较，字符串比较只要错配就立刻返回
            return -1
        elif ab == ba:
            return 0
        else:
            return 1

    if not isinstance(nums, list) or len(nums) <= 0:
        return

    numsOfStr = [str(num) for num in nums]
    numsOfStr = sorted(numsOfStr, key=cmp_to_key(compare))

    return ''.join(numsOfStr)


import unittest

class TestPrintMinNumber(unittest.TestCase):
    def test_print_min_number(self):
        self.assertEqual(printMinNumber([3,5,1,4,2]), '12345')
        self.assertEqual(printMinNumber([3,32,321]), '321323')
        self.assertEqual(printMinNumber([3,323,32123]), '321233233')
        self.assertEqual(printMinNumber([1,11,111]), '111111')
        self.assertEqual(printMinNumber([321]), '321')
        self.assertEqual(printMinNumber(None), None)


if __name__ == '__main__':
    unittest.main()
