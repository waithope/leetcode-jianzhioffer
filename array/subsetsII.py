
## Description
## Given a collection of integers that might contain *duplicates*, nums,
## return all possible subsets (the power set).
# Input: [1,2,2]
# Output:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

def subsetsWithDup(nums):
  size = len(nums)
  if size == 0 or nums is None:
    return [[]]

  nums.sort()
  res = [[]]
  for i in range(size):
    if i == 0 or nums[i] != nums[i-1]:
      l = len(res)
    for j in range(len(res)-l, len(res)): # when encountered duplicates, just add
      res.append(res[j]+[nums[i]])       # it to the last added subsets
  return res


import unittest

class TestSubsetsWithDup(unittest.TestCase):
  def test_subsets_with_dup(self):
    self.assertEqual(subsetsWithDup([1,2,2]), [[],[1],[2],[1,2],[2,2],[1,2,2]])
    self.assertEqual(subsetsWithDup([4,4,4,1,4]), [[],[1],[4],[1,4],[4,4],[1,4,4],
                                    [4,4,4],[1,4,4,4],[4,4,4,4],[1,4,4,4,4]])


if __name__ == '__main__':
  unittest.main()