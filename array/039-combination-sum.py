## Description
## Given a set of candidate numbers (candidates) (without duplicates)
## and a target number (target), find all unique combinations in candidates
## where the candidate numbers sums to target.
## The same repeated number may be chosen from candidates unlimited number of times.
## Note:
## All numbers (including target) will be positive integers.
## The solution set must not contain duplicate combinations.

## Input: candidates = [2,3,6,7], target = 7,
## A solution set is:
## [
##   [7],
##   [2,2,3]
## ]
## Input: candidates = [2,3,5], target = 8,
## A solution set is:
## [
##   [2,2,2,2],
##   [2,3,3],
##   [3,5]
## ]


def combinationSum(candidates, target):
  """
  :type candidates: List[int]
  :type target: int
  :rtype: List[List[int]]
  """

  def backtrack(nums, res, path, remain, start):
    if remain < 0:
      return
    if remain == 0:
      res.append(path)
      return
    for i in range(start, len(nums)):
      backtrack(nums, res, path+[nums[i]], remain-nums[i], i)   # start = i reuse same element

  candidates.sort()
  res = []
  backtrack(candidates, res, [], target, 0)
  return res


import unittest

class TestCombinationSum(unittest.TestCase):
  def test_combination_sum(self):
    self.assertEqual(combinationSum([1],1), [[1]])
    self.assertEqual(combinationSum([1,2],4), [[1,1,1,1],[1,1,2],[2,2]])
    self.assertEqual(combinationSum([2,3,5],8), [[2,2,2,2],[2,3,3],[3,5]])
    self.assertEqual(combinationSum([2,3,6,7],7), [[2,2,3],[7]])


if __name__ == '__main__':
  unittest.main()

