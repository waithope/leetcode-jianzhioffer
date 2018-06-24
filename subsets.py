
## Description
## Given a set of *distinct* integers, nums,
## return all possible subsets (the power set).
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

# iterative
def subsets(nums):
  size = len(nums)
  if size == 0 or nums is None:
    return [[]]

  res = [[]]
  for num in nums:
    res += [item+[num] for item in res]
  return res

def subsets_bit(nums):
  size = len(nums)
  if size == 0 or nums is None:
    return [[]]
  res = []
  for i in range(1<<size):
    temp = []
    for j in range(size):
      if i & (1 << j):
        temp.append(nums[j])
    res.append(temp)
  return res


import unittest

class TestSubsets(unittest.TestCase):
  def test_subsets(self):
    self.assertEqual(subsets_bit([]), [[]])
    self.assertEqual(subsets_bit([0,3]), [[],[0],[3],[0,3]])
    self.assertEqual(subsets_bit([1, 2, 3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])


if __name__ == '__main__':
  unittest.main()