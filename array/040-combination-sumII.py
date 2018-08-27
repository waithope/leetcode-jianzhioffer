## Description
## Given a collection of candidate numbers (candidates) and a target number (target),
## find all unique combinations in candidates where the candidate numbers sums to target.
## Each number in candidates may only be used once in the combination.
## Note:
## All numbers (including target) will be positive integers.
## The solution set must not contain duplicate combinations.
## Example 1:
## Input: candidates = [10,1,2,7,6,1,5], target = 8,
## A solution set is:
## [
##   [1, 7],
##   [1, 2, 5],
##   [2, 6],
##   [1, 1, 6]
## ]
## Example 2:
## Input: candidates = [2,5,2,1,2], target = 5,
## A solution set is:
## [
##   [1,2,2],
##   [5]
## ]


def combinationSum2(candidates, target):
  """
  :type candidates: List[int]
  :type target: int
  :rtype: List[List[int]]
  """
  def backtrack(nums, remain, path, res, start):
    if remain < 0:
      return
    if remain == 0:
      res.append(path)
      return
    for i in range(start, len(nums)):
      if i > start and nums[i] == nums[i-1]: continue
      backtrack(nums, remain-nums[i], path+[nums[i]], res, i+1)

  candidates.sort()
  res = []
  backtrack(candidates, target, [], res, 0)
  return res


import unittest

class TestCombinationSumII(unittest.TestCase):
  def test_combination_sumII(self):
    self.assertEqual(combinationSum2([10,1,2,7,6,1,5],8), [[1,1,6],[1,2,5],[1,7],[2,6]])
    self.assertEqual(combinationSum2([2,5,2,1,2],5), [[1,2,2],[5]])


if __name__ == '__main__':
  unittest.main()