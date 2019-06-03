# -*- coding:utf-8 -*-
'''
        n个骰子的点数
============================
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值
出现的概率。
'''

def dicesProbability_Recursively(n):
    '''
    思路：所有n个骰子的点数和最小值为n，最大值为6*n。n个骰子所有点数的排列数
    为6^n。因此，要统计点数s出现的概率，首先要计算点数s出现的次数，将点数s
    出现的次数除以6^n，即该点数s出现的概率。其中一个思想就是利用递归，将n个
    骰子分成两部分，第一部分只有一个骰子，第二部分为n-1个骰子。计算第一个骰子
    的每一种点数和剩下部分的n-1个骰子来计算点数和。接下来，把剩下部分的n-1个
    骰子分为两部分，第一部分1个骰子，第二部分为n-2个骰子。按照这种递归的思想，
    递归直到最后只有1个骰子为止。
    按照上述思路，设n个骰子某次投掷点数和为s的出现次数为s，那么F(n, s)等于n-1个
    骰子投掷的点数和s-1、s-2、s-3、s-4、s-5以及s-6的次数总和。公式表示为：
    F(n, s)=F(n-1, s-1)+F(n-1, s-2)+F(n-1, s-3)+F(n-1, s-4)+F(n-1, s-5)
    +F(n-1, s-6)
    '''
    def countNum(n, s):
        if s < n or s > 6*n:
            return 0
        if n == 1:
            return 1
        else:
            return (countNum(n - 1, s - 1) + countNum(n - 1, s - 2)
                    + countNum(n - 1, s - 3) + countNum(n - 1, s - 4)
                    + countNum(n - 1, s - 5) + countNum(n - 1, s - 6))

    total = 6 ** n
    for i in range(n, 6 * n + 1):
        print("P(s = %d) = %d / %d = %f" % (i, countNum(n, i), total,
                                            countNum(n, i) / total))


def dicesProbability_Iteratively(n):
    '''
    思路：递归的方法时间效率很低，时间复杂度为O(6^n)。利用两个数组交替更新的循环
    计算方法可以大大低降低时间复杂度。具体的方法流程见程序注释。
    '''
    if not isinstance(n, int) or n < 1:
        return

    diceMaxValue = 6
    probability = []
    for i in range(2):
        # 创建两个数组用于存储所有可能点数出现的次数，数组下标表示可能的点数s，
        # 而该下标对应的值表示该点数s出现的次数
        probability.append([0] * (diceMaxValue * n + 1))

    flag = 0
    # 投掷第一个骰子时所有可能点数出现的次数均为1
    for i in range(1, diceMaxValue + 1):
        probability[flag][i] = 1
    # 从第二个骰子开始，两个数组交替更新，flag = 1 - flag 交替更新标志
    for i in range(2, n + 1):
        for j in range(i):
            # 投掷第i个骰子时，其点数和的最小值为i，小于i为不可能时间，将对应下标的值置0
            probability[1 - flag][j] = 0
        for k in range(i, i * diceMaxValue + 1):
            # 对即将更新的对应位置清0，如果不清零，下一步的+=计算得不到正确结果
            probability[1 - flag][k] = 0
            for t in range(1, diceMaxValue + 1):
                # 投掷i个骰子，其点数为k出现的次数为上一次更新的数组k-1、k-2、k-3、
                # k-4、k-5、k-6点数出现次数的总和
                probability[1 - flag][k] += probability[flag][k - t]
        flag = 1 - flag

    total = diceMaxValue ** n
    for i in range(n, diceMaxValue * n + 1):
        print("P(s = %d) = %d / %d = %f" % (i, probability[flag][i], total,
                                            probability[flag][i] / total))


import time
if __name__ == '__main__':
    start = time.time()
    dicesProbability_Recursively(3)
    print('the time it takes %f s' % (time.time() - start))
    print('======================')
    start = time.time()
    dicesProbability_Iteratively(3)
    print('the time it takes %f s' % (time.time() - start))


