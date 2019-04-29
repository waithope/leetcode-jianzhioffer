# -*- coding:utf-8 -*-
'''
    把数字翻成字符串
=======================
给定一个数字，我们按照如下规则把它翻译为字符串：0翻译成"a"，1翻译成"b"，……，
11翻译成"l"，……，25翻译成"z"。一个数字可能有多个翻译。例如12258有5种不同的翻译，
它们分别是"bccfi"、"bwfi"、"bczi"、"mcfi"和"mzi"。
请编程实现一个函数用来计算一个数字有多少种不同的翻译方法。
'''


def translationCount(num):
    '''
    思路：我们以12258为例大致分析一下如何计算不同翻译的数目。对于第一步，我们有
    两种不同的选择进行翻译，第一种选择是数字1单独翻译成"b"，后面剩下数字2258；
    第二种选择是数字1和2合在一起翻译成"m"，后面剩下数字258。接着针对不同的选择
    来翻译剩下的数字。显然，这是一个递归的过程。我们定义函数f(i)表示从第i位数字
    开始有多少种不同的翻译数目。函数表达式f(i)=f(i+1)+g(i,i+1)*f(i+2)，
    g(i,i+1)表示第i位数字和第i+1位数字合在一起是否在10~25之间，如果是，则
    g(i,i+1)=1；反之，则为0。那究竟这个公式如何理解呢？我通过258这个例子来进行
    说明，我们从数字末尾开始，从右往左计算不同翻译数目（从数字第一位开始，有的
    子问题是重复的，比如1，2258；12，258；1，2，258；258这个子问题重复了）。
    首先，创建一个与258位数相同大小的数组dp，用于保存从当前的每一个位置开始有多少
    种不同的翻译数目，首先从后往前遍历，末尾数字是8，由于末尾数字没有第i+1个位置，
    所以dp[2]=1；接着，往前遍历，当前数字是5，由于5与8不能组成范围在10-25的数字，
    dp[1]=dp[2]=1；然后，继续往前遍历，当前数字是2，由于2与5能组成范围在10-25的
    数字，所以dp[0]=dp[1]+dp[2]=2；那么具体的实际的公式的f(i+1)+g(i,i+1)*f(i+2)，
    就是dp[1]+1*dp[2]，dp[1]就表示当单独翻译2时，剩下的数字58有多少种不同的翻译；
    dp[2]就表示2和5合在一起翻译，剩下的数字8有多少种翻译；两者翻译数目之和即为当前位置
    数字的总的不同翻译数目。
    '''
    if not isinstance(num, int) or num < 0:
        return 0

    numOfStr = str(num)
    length = len(numOfStr)
    dp = [0] * length
    for i in range(length-1, -1, -1):
        if i == length - 1:
            dp[i] = 1
            continue

        count = dp[i+1]
        val = (ord(numOfStr[i]) - ord('0')) * 10 + (ord(numOfStr[i+1]) - ord('0'))
        if i == length - 2:
            if val >= 10 and val <= 25:
                count += 1
        else:
            if val >= 10 and val <= 25:
                count += dp[i+2]
        dp[i] = count
    return dp[0]


import unittest

class TestTranslationCount(unittest.TestCase):
    def test_translation_count(self):
        self.assertEqual(translationCount(0), 1)
        self.assertEqual(translationCount(10), 2)
        self.assertEqual(translationCount(125), 3)
        self.assertEqual(translationCount(126), 2)
        self.assertEqual(translationCount(426), 1)
        self.assertEqual(translationCount(100), 2)
        self.assertEqual(translationCount(101), 2)
        self.assertEqual(translationCount(12258), 5)
        self.assertEqual(translationCount(-100), 0)


if __name__ == '__main__':
    unittest.main()
