## Description
## Say you have an array for which the ith element is
## the price of a given stock on day i.
## If you were only permitted to complete at most one transaction
## (i.e., buy one and sell one share of the stock),
## design an algorithm to find the maximum profit.

## Input: [7,1,5,3,6,4]
## Output: 5
## Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
##              Not 7-1 = 6, as selling price needs to be larger than buying price.
## Input: [7,6,4,3,1]
## Output: 0
## Explanation: In this case, no transaction is done, i.e. max profit = 0.

def maxProfit(prices):
  """
  :type prices: List[int]
  :rtype: int
  """
  #n = len(prices)
  #if n <= 1:
  #    return 0
  #
  #maxProfit = 0
  #prev = prices[0]
  #for i in range(1, n):
  #    diff = prices[i] - prev
  #    if diff < 0:
  #        prev = prices[i]
  #    if diff > maxProfit:
  #        maxProfit = diff
  #return maxProfit

  if prices == []:
    return 0
  maxProfit = 0
  low = prices[0]
  for p in prices:
    if p < low:
      low = p
    elif p-low > maxProfit:
      maxProfit = p - low
  return maxProfit


import unittest

class TestBestTimetoSellStock(unittest.TestCase):
  def test_best_time_to_sell_stock(self):
    self.assertEqual(maxProfit([]), 0)
    self.assertEqual(maxProfit([7,6,4,3,1]), 0)
    self.assertEqual(maxProfit([7,1,5,3,6,4]), 5)


if __name__ == '__main__':
  unittest.main()