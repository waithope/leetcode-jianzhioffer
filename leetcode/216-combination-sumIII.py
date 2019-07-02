## Description
## Find all possible combinations of k numbers that add up to a number n,
## given that only numbers from 1 to 9 can be used
## and each combination should be a unique set of numbers.
## Note:
## All numbers will be positive integers.
## The solution set must not contain duplicate combinations.
## Input: k = 3, n = 7
## Output: [[1,2,4]]
## Input: k = 3, n = 9
## Output: [[1,2,6], [1,3,5], [2,3,4]]


def combinationSum3(k, n):
  """
  :type k: int
  :type n: int
  :rtype: List[List[int]]
  """
  def backtrack(nums, path, remain, start):
    if remain < 0:
      return
    if remain == 0:
      if len(path) == k:
        res.append(path)
      return
    for i in range(start, len(nums)):
      backtrack(nums, path+[nums[i]], remain-nums[i], i+1)

  array = [i for i in range(1, 10)]
  res = []
  backtrack(array, [], n, 0)
  return res


import unittest

class Test_Combination_SumIII(unittest.TestCase):
  def test_combination_sumiii(self):
    self.assertEqual(combinationSum3(3, 7), [[1,2,4]])
    self.assertEqual(combinationSum3(3, 9), [[1,2,6],[1,3,5],[2,3,4]])


if __name__ == '__main__':
  unittest.main()