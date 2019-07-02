## Description
## Given a sorted array nums, remove the duplicates in-place
## such that duplicates appeared at most twice and return the new length.
## Do not allocate extra space for another array, you must do this
## by modifying the input array in-place with O(1) extra memory.
## Given nums = [1,1,1,2,2,3],
## Your function should return length = 5, with the first five elements of nums
## being 1, 1, 2, 2 and 3 respectively.

def removeDuplicates(nums):
  """
  :type nums: List[int]
  :rtype: int
  """

  #if not nums:
  #    return 0
  #
  #tail, limit = 0, 1
  #for i in range(1, len(nums)):
  #    if nums[i] == nums[i-1]:
  #        limit += 1
  #        if limit > 2:
  #            continue
  #        tail += 1
  #    else:
  #        tail += 1
  #        limit = 1
  #    nums[tail] = nums[i]
  #return tail+1

  tail = 0
  for num in nums:
    if tail < 2 or num > nums[tail-2]:     # skip the duplicates
      nums[tail] = num
      tail += 1
  return nums[:tail]


import unittest

class TestRemoveDuplicatesII(unittest.TestCase):
  def test_remove_duplicatesII(self):
    self.assertEqual(removeDuplicates([]), [])
    self.assertEqual(removeDuplicates([1,1,1,2,2,3]), [1,1,2,2,3])
    self.assertEqual(removeDuplicates([0,0,1,1,1,1,2,3,3]), [0,0,1,1,2,3,3])


if __name__ == '__main__':
  unittest.main()
