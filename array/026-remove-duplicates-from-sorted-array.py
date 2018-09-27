'''
  Remove Duplicates from Sorted Array
=========================================
Given a sorted array nums, remove the duplicates in-place
such that each element appear only once and return the new length.
Do not allocate extra space for another array,
you must do this by modifying the input array in-place with O(1) extra memory

Example 1:
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements
of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.

Example 2:
Given nums = [0,0,1,1,1,2,2,3,3,4],
Your function should return length = 5, with the first five elements of nums
being modified to 0, 1, 2, 3, and 4 respectively.
It doesn't matter what values are set beyond the returned length.
'''

def removeDuplicates(nums):
  """
  :type nums: List[int]
  :rtype: int
  """
  if nums == []:
    return 0
  tail = 0
  for i in range(1, len(nums)):
    if nums[i] == nums[i-1]:
      continue
    else:
      tail += 1
      nums[tail] = nums[i]
  return tail+1

import unittest

class TestRemoveDuplicates(unittest.TestCase):
  def test_remove_duplicates(self):
    self.assertEqual(removeDuplicates([1,1,2]), 2)
    self.assertEqual(removeDuplicates([0,0,1,1,1,2,2,3,3,4]), 5)


if __name__ == '__main__':
  unittest.main()