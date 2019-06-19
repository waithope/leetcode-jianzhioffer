## Description
## Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
## find the one that is missing from the array.
## Input: [3,0,1]
## Output: 2
## Input: [9,6,4,2,3,5,7,0,1]
## Output: 8
## Your algorithm should run in linear runtime complexity and
## implement it using only constant extra space complexity?

def missingNumber(nums):
  """
  :type nums: List[int]
  :rtype: int
  """
  n = len(nums) + 1
  target = n*(n-1) / 2
  return target - sum(nums)


import unittest

class TestMissingNumber(unittest.TestCase):
  def test_missing_number(self):
    self.assertEqual(missingNumber([0]), 1)
    self.assertEqual(missingNumber([3,0,1]), 2)
    self.assertEqual(missingNumber([6,5,4,3,2,1]), 0)
    self.assertEqual(missingNumber([9,6,4,2,3,5,7,0,1]), 8)


if __name__ == '__main__':
  unittest.main()