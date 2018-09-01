## Description
## Given an array with integers.
## Find two non-overlapping subarrays A and B,
## which |SUM(A) - SUM(B)| is the largest.
## Return the largest difference.
## The subarray should contain at least one number, O(n) time and O(n) space.
## Example
## For [1, 2, -3, 1], return 6.

def maxDiffSubArray(nums):
  if nums == []:
    return 0

  size = len(nums)
  # leftMax = leftMin = rightMax = rightMin = [0 for i in range(size)]
  leftMax, leftMin = [0 for i in range(size)], [0 for i in range(size)]
  rightMax, rightMin = [0 for i in range(size)], [0 for i in range(size)]
  maxRes, minRes, maxSum, minSum, sum = -(2**32), 2**32, 0, 0, 0
  for i in range(size):
    sum += nums[i]
    maxRes = max(maxRes, sum - minSum)
    minSum = min(minSum, sum)
    leftMax[i] = maxRes

    minRes = min(minRes, sum - maxSum)
    maxSum = max(maxSum, sum)
    leftMin[i] = minRes

  maxRes, minRes, maxSum, minSum, sum = -(2**32), 2**32, 0, 0, 0
  for i in range(size-1, -1, -1):
    sum += nums[i]
    maxRes = max(maxRes, sum - minSum)
    minSum = min(minSum, sum)
    rightMax[i] = maxRes

    minRes = min(minRes, sum - maxSum)
    maxSum = max(maxSum, sum)
    rightMin[i] = minRes

  res = -(2**32)
  for i in range(size - 1):
    res = max(res, abs(leftMax[i] - rightMin[i + 1]),
              abs(leftMin[i] - rightMax[i + 1]))

  return res


import unittest

class MaxDiffSubArray(unittest.TestCase):
  def test_max_diff_subarray(self):                 # test method name should start with test
    self.assertEqual(maxDiffSubArray([]), 0)        # i.e. test_bla_bla(self):
    self.assertEqual(maxDiffSubArray([1, 2, -3, 1]), 6)
    self.assertEqual(maxDiffSubArray([-5, -4]), 1)
    self.assertEqual(maxDiffSubArray([2, -1, -2, 1, -4, 2, 8]), 16)
    self.assertEqual(maxDiffSubArray([-2, -3, 4, -1, -2, 1, 5, -3]), 12)


if __name__ == '__main__':
  unittest.main()