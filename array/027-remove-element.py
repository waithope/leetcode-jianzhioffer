## Description
## Given an array nums and a value val, remove all instances of
## that value in-place and return the new length.
## Do not allocate extra space for another array, you must do this
## by modifying the input array in-place with O(1) extra memory.
## The order of elements can be changed. It doesn't matter
## what you leave beyond the new length.

## Given nums = [3,2,2,3], val = 3,
## Your function should return length = 2
## Given nums = [0,1,2,2,3,0,4,2], val = 2,
## Your function should return length = 5

def removeElement(nums, val):
  """
  :type nums: List[int]
  :type val: int
  :rtype: int
  """

  n = len(nums)
  tail = 0
  for i in range(n):
    if nums[i] != val:
      nums[tail] = nums[i]
      tail += 1
  return nums[:tail]


import unittest

class TestRemoveElement(unittest.TestCase):
  def test_remove_element(self):
    self.assertEqual(removeElement([0,1,2], 0), [1,2])
    self.assertEqual(removeElement([3,2,2,3], 3), [2,2])
    self.assertEqual(removeElement([0,1,2,2,3,0,4,2], 2), [0,1,3,0,4])


if __name__ == '__main__':
  unittest.main()

