## Description
## Given an array of integers and an integer k, find out
## whether there are two distinct indices i and j in the array
## such that nums[i] = nums[j] and the absolute difference
## between i and j is at most k.
## Input: nums = [1,2,3,1], k = 3
## Output: true
## Input: nums = [1,0,1,1], k = 1
## Output: true
## Input: nums = [1,2,3,1,2,3], k = 2
## Output: false

def containsNearbyDuplicate(nums, k):
  """
  :type nums: List[int]
  :type k: int
  :rtype: bool
  """
  #for i in range(len(nums)):
  #    for j in range(i+1, i+k+1, 1):
  #        if j == len(nums):
  #            break
  #        if nums[i] == nums[j]:
  #            return True
  #return False

  c = {}
  for idx, num in enumerate(nums):
    if num in c and (idx - c[num]) <= k:
      return True
    c[num] = idx
  return False


import unittest

class TestContainDuplicatesII(unittest.TestCase):
  def test_contain_duplicatesII(self):
    self.assertEqual(containsNearbyDuplicate([1,2,3,1], 3), True)
    self.assertEqual(containsNearbyDuplicate([1,0,1,1], 1), True)
    self.assertEqual(containsNearbyDuplicate([1,2,3,1,2,3], 2), False)


if __name__ == '__main__':
  unittest.main()
