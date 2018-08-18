
## Description
## Given an integer array nums, find the contiguous subarray
## (containing at least one number) which has the largest sum and return its sum.
## Input: [-2,1,-3,4,-1,2,1,-5,4],
## Output: 6
## Explanation: [4,-1,2,1] has the largest sum = 6.

## Brute Force
def maxSubArray_BF(nums):
  """
  :type nums: List[int]
  :rtype: int
  """
  maximum = nums[0]
  for i in range(len(nums)):
    sum = 0
    for j in range(i, len(nums)):
      sum += nums[j]
      maximum = max(maximum, sum)
  return maximum


## Divide and Conquer
def maxSubArray_DC(nums):
  """
  :type nums: List[int]
  :rtype: int
  """
  maxsum = [0]*len(nums)    # extra space
  maxsum[0] = nums[0]
  max_global_sum = nums[0]
  for i in range(1, len(nums)):
    maxsum[i] = max(nums[i], nums[i] + maxsum[i-1])
    max_global_sum = max(max_global_sum, maxsum[i])
  return max_global_sum

def maxSubArray(nums):
  maxsum = -(2**32)
  s = 0
  for num in nums:
    s += num
    if s <= num:
      s = num
    if s > maxsum:
      maxsum = s
  return maxsum


import unittest

class TestMaximumSubarray(unittest.TestCase):
  def test_max_sub(self):
    self.assertEqual(maxSubArray_DC([-2]), -2)
    self.assertEqual(maxSubArray_DC([-2, 1]), 1)
    self.assertEqual(maxSubArray_DC([2, 3, -1, -20, 5, 10]), 15)
    self.assertEqual(maxSubArray_DC([-2,1,-3,4,-1,2,1,-5,4]), 6)


if __name__ == '__main__':
  unittest.main(verbosity=2)
