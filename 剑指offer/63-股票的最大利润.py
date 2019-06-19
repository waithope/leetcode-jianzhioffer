# -*- coding:utf-8 -*-
'''
        股票的最大利润
=============================
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖交易该股票可能获得的
利润是多少？例如一只股票在某些时间节点的价格为{9, 11, 8, 5, 7, 12, 16, 14}。
如果我们能在价格为5的时候买入并在价格为16时卖出，则能收获最大的利润11。
'''

def maxStockProfit(nums):
    '''
    思路：股票交易的利润来自买入和卖出的差价，因此这个问题就是求出所有数对中的
    最大差值。蛮力法就是遍历所有数对找出最大差值，这种方法的时间复杂度是O(n^2)。
    另一种更加简洁高效的方法就是当数组中第i个数字为卖出价时，记录前i-1个数字中
    的最低买入价格，并通过比较记录当前的最大差值即可。
    '''
    if not isinstance(nums, list) or len(nums) < 2:
        return 0

    buy = nums[0]
    maxDiff = nums[1] - buy
    for i in range(2, len(nums)):
        if nums[i - 1] < buy:
            buy = nums[i - 1]

        diff = nums[i] - buy
        if diff > maxDiff:
            maxDiff = diff
    return maxDiff


import unittest

class TestMaxStockProfit(unittest.TestCase):
    def test_max_stock_profit(self):
        self.assertEqual(maxStockProfit([2,4]), 2)
        self.assertEqual(maxStockProfit(None), 0)
        self.assertEqual(maxStockProfit([4,1,3,2,5]), 4)
        self.assertEqual(maxStockProfit([1,2,4,7,11,16]), 15)
        self.assertEqual(maxStockProfit([16,11,7,4,2,1]), -1)
        self.assertEqual(maxStockProfit([16,16,16,16,16]), 0)
        self.assertEqual(maxStockProfit([9,11,5,7,16,1,4,2]), 11)
        self.assertEqual(maxStockProfit([9,11,5,7,16,1,4,2]), 11)


if __name__ == '__main__':
    unittest.main()