
## Description
## Given an integer array nums, find the contiguous subarray within an array
## (containing at least one number) which has the largest product.
## Input: [2,3,-2,4]
## Output: 6
## Explanation: [2,3] has the largest product 6.

def maxProduct(nums):
  """
  :type nums: List[int]
  :rtype: int
  """
  maximum = nums[0]
  curr_max = curr_min = maximum
  for i in range(1, len(nums)):
    if nums[i] < 0:
      curr_max, curr_min = curr_min, curr_max

    curr_max = max(nums[i], curr_max*nums[i])
    curr_min = min(nums[i], curr_min*nums[i])

    maximum = max(maximum, curr_max)
  return maximum


import unittest

class TestProduct(unittest.TestCase):
  def test_subarray_product(self):
    self.assertEqual(maxProduct([2, 3, -2, 4]), 6)
    self.assertEqual(maxProduct([-2, 3, -4]), 24)
    self.assertEqual(maxProduct([0, 2]), 2)
    self.assertEqual(maxProduct([2]), 2)
    self.assertEqual(maxProduct([2, 3, -2, 5, 4, 9, -4]), 8640)


if __name__ == '__main__':
  unittest.main()

