## Description
## Say you have an array for which the ith element is
## the price of a given stock on day i.
## Design an algorithm to find the maximum profit. You may complete
## as many transactions as you like (i.e., buy one and sell one share of
## the stock multiple times).
## Note: You may not engage in multiple transactions at the same time
## (i.e., you must sell the stock before you buy again).
## Input: [7,1,5,3,6,4]
## Output: 7
## Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
## Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

def maxProfit(prices):
  """
  :type prices: List[int]
  :rtype: int
  """
  #n = len(prices)
  #if n < 2:
  #    return 0
  #
  #profit = 0
  #low = prices[0]
  #for i in range(1, n-1):
  #    if prices[i] < low:
  #        low = prices[i]
  #    elif prices[i+1] < prices[i]:
  #        profit += prices[i] - low
  #        low = prices[i]
  #if prices[-1] >= prices[-2]:
  #    profit += prices[-1] - low
  #return profit

  if not prices:
    return 0

  profit, low = 0, prices[0]
  for price in prices:
    if price > low:
      profit += price - low
      low = price
    else:
      low = price
  return profit


import unittest

class TestMaxProfit(unittest.TestCase):
  def test_max_profit(self):
    self.assertEqual(maxProfit([]), 0)
    self.assertEqual(maxProfit([1]), 0)
    self.assertEqual(maxProfit([1,2,3,4,5]), 4)
    self.assertEqual(maxProfit([7,1,5,3,6,4]), 7)
    self.assertEqual(maxProfit([1,9,6,9,1,7,1,1,9,9,9]), 25)


if __name__ == '__main__':
  unittest.main()