# -*- coding:utf-8 -*-
'''
    剪绳子
=============
给你一根长度为n的绳子，请把绳子剪成m段（m,n都是整数，m>1，n>1），每段绳子的长度
记为k[0],k[1],...,k[m]。请问k[0]*k[1]*...*k[m]可能的最大乘积是多少？例如，
当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
'''


def maxProductCutRope_DP(n):
    '''
    剪绳子的动态规划方法
    时间O(n^2), 空间O(n)
    '''
    if not isinstance(n, int) or n < 2:
        return 0

    if n == 2:
        return 1
    if n == 3:
        return 2

    # 用prodcut保存绳子长度为i时的最大值
    products = [0 for _ in range(n+1)]
    # 长度大于3时，子问题为f(1)，f(2)，f(3)时其最大值为自身长度
    products[1], products[2], products[3] = 1, 2, 3

    for i in range(4, n+1):
        for j in range(1, i // 2 + 1):
            prod = products[j] * products[i-j]
            if prod > products[i]:
                products[i] = prod
    return products[n]


def maxProductCutRope_Greedy(n):
    '''
    剪绳子的贪心算法版是通过公式求解乘积最大的问题
    时间O(1), 空间O(1)
    证明：
    当n=1时，由于题目要求至少剪一次，该种情况作废，程序中返回0
    当2<=n<=4时，n=4，剪成2段或者保留；n=3,2时，保留；
    当n>=5时，3(n-3)>=2(n-2)>n, 等号在n=5时取得；
    证明到这里，可能会想能不能剪成其他大小会更好，比如9，假如剪成
    9以后不剪是不能得到乘积最大的，因为3(9-3)>9的，所以只要其他
    大小不小于5就能够继续往下剪。
    '''

    if not isinstance(n, int) or n <= 1:
        return 0

    if n == 2:
        return 1
    if n == 3:
        return 2

    timesOf2, timesOf3 = 0, 0
    timesOf3 = n // 3
    if (n - 3 * timesOf3) == 1:
        timesOf3 -= 1
    timesOf2 = (n - 3 * timesOf3) // 2

    return (3**timesOf3) * (2**timesOf2)

import unittest

class TestMaxProductCutRopeDp(unittest.TestCase):
    def test_max_product_cut_rope_dp(self):
        self.assertEqual(maxProductCutRope_DP(1), 0)
        self.assertEqual(maxProductCutRope_DP(2), 1)
        self.assertEqual(maxProductCutRope_DP(3), 2)
        self.assertEqual(maxProductCutRope_DP(4), 4)
        self.assertEqual(maxProductCutRope_DP(8), 18)
        self.assertEqual(maxProductCutRope_DP(50), 86093442)
        self.assertEqual(maxProductCutRope_Greedy(1), 0)
        self.assertEqual(maxProductCutRope_Greedy(2), 1)
        self.assertEqual(maxProductCutRope_Greedy(3), 2)
        self.assertEqual(maxProductCutRope_Greedy(4), 4)
        self.assertEqual(maxProductCutRope_Greedy(8), 18)
        self.assertEqual(maxProductCutRope_Greedy(50), 86093442)

if __name__ == '__main__':
    unittest.main()
