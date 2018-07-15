
## Description
## given an array A of positive integers, and two positive integers L and R (L <= R).
## Return the number of (contiguous, non-empty) subarrays
## such that the value of the maximum array element in that subarray
## is at least L and at most R.

## Example :
## Input:
## A = [2, 1, 4, 3]
## L = 2
## R = 3
## Output: 3
## Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].

## Time: O(n) Space: O(1)
def numSubarrayBoundedMax(A, L, R):
  """
  :type A: List[int]
  :type L: int
  :type R: int
  :rtype: int
  """
  res, dp = 0, 0
  prev = -1
  for i in range(len(A)):
    if A[i] < L:
      res += dp
    elif A[i] > R:
      dp = 0
      prev = i
    else:
      dp = i - prev
      res += dp
  return res


import unittest

class TestNumSubarraysBoundedMax(unittest.TestCase):
  def test_num_subarrays_bounded_max(self):
    self.assertEqual(numSubarrayBoundedMax([2,3,4],2,5), 6)      # to be verified
    self.assertEqual(numSubarrayBoundedMax([2,1,4,3],2,3), 3)
    self.assertEqual(numSubarrayBoundedMax([2,9,2,5,6],2,8), 7)
    self.assertEqual(numSubarrayBoundedMax([2,1,4,2,3],2,3), 5)


if __name__ == '__main__':
  unittest.main()
