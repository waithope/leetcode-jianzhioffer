## Description
## Given an array of n positive integers and a positive integer s,
## find the minimal length of a contiguous subarray of which the sum ≥ s.
## If there isn't one, return 0 instead.
## Input: s = 7, nums = [2,3,1,2,4,3]
## Output: 2
## Explanation: the subarray [4,3] has the minimal length under the problem constraint.
## If you have figured out the O(n) solution, try coding another solution
## of which the time complexity is O(n log n).

def minSubArrayLen(s, nums):
  """
  :type s: int
  :type nums: List[int]
  :rtype: int
  """
  ## brute force O(N**3)
  #minlen = len(nums) + 1
  #for i in range(len(nums)):
  #    for j in range(i, len(nums)):
  #        sums = 0
  #        for k in range(i, j+1):
  #            sums += nums[k]
  #            if sums >= s:
  #                minlen = min(minlen, k-i+1)
  #return minlen if minlen <= len(nums) else 0

  ## brute force O(N**2) space O(N)
  #if not nums:
  #    return 0
  #
  #sums, minlen = [0]*len(nums), len(nums)+1
  #sums[0] = nums[0]
  #for i in range(1, len(nums)):
  #    sums[i] = sums[i-1] + nums[i]
  #for i in range(len(nums)):
  #    for j in range(i, len(nums)):
  #        sum_ = sums[j] - sums[i] + nums[i]
  #        if sum_ >= s:
  #            minlen = min(minlen, j-i+1)
  #return minlen if minlen <= len(nums) else 0

  ## using binary search O(Nlog(N)), space O(N)
  # def lower_index(low, high, target):
  #   while low < high:
  #     mid = low + (high-low) // 2
  #     if target == sums[mid]:
  #       return mid
  #     elif target < sums[mid]:
  #       high = mid
  #     else:
  #       low = mid + 1
  #   return low

  # if not nums:
  #   return 0

  # sums, minlen = [0]*(len(nums)+1), len(nums)+1
  # for i in range(1, len(nums)+1):
  #   sums[i] = sums[i-1] + nums[i-1]

  # for i in range(1, len(sums)):
  #   to_find = s + sums[i-1]
  #   bound = lower_index(0, len(sums), to_find)
  #   if bound != len(sums):
  #     minlen = min(minlen, bound-i+1)
  # return minlen if minlen <= len(nums) else 0


  ## time complexity O(N), space O(1), using two pointers
  left, sums, minlen = 0, 0, len(nums)+1
  for i in range(len(nums)):
    sums += nums[i]
    while sums >= s:
      minlen = min(minlen, i-left+1)
      sums -= nums[left]
      left += 1
  return minlen if minlen <= len(nums) else 0


import unittest

class TestMinSubArrayLen(unittest.TestCase):
  def test_min_subarray_len(self):
    self.assertEqual(minSubArrayLen(100,[]), 0)
    self.assertEqual(minSubArrayLen(4,[1,4,4]), 1)
    self.assertEqual(minSubArrayLen(11,[1,2,3,4,5]), 3)
    self.assertEqual(minSubArrayLen(7,[2,3,1,2,4,3]), 2)

if __name__ == '__main__':
  unittest.main()