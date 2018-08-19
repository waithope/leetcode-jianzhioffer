## Description
## Suppose an array sorted in ascending order is rotated
## at some pivot unknown to you beforehand.
## (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
## This is a follow up problem to Search in Rotated Sorted Array,
## where nums may contain duplicates.
## You are given a target value to search.
## If found in the array return true, otherwise return false.

def search(nums, target):
  """
  :type nums: List[int]
  :type target: int
  :rtype: bool
  """
  l, h = 0, len(nums)-1

  while l <= h:
    m = (l+h) // 2
    if nums[m] == target:
      return True
    elif nums[l] < nums[m]:
      if nums[l] <= target < nums[m]:
        h = m - 1
      else:
        l = m + 1
    elif nums[l] == nums[m]:   # [1,3,1,1,1] move forward one cell
      l += 1
    else:
      if nums[m] < target <= nums[h]:
        l = m + 1
      else:
        h = m - 1
  return False


import unittest

class TestSearchInRotatedSortedArrayII(unittest.TestCase):
  def test_search_in_rotated_sorted_arrayII(self):
    self.assertEqual(search([5,1,3], 5), True)
    self.assertEqual(search([3,1,1], 0), False)
    self.assertEqual(search([1,3,1,1,1], 3), True)
    self.assertEqual(search([4,5,6,7,0,1,2], 0), True)
    self.assertEqual(search([4,5,6,7,0,1,2], 3), False)
    self.assertEqual(search([2,2,6,7,8,9,10,1,2], 2), True)


if __name__ == '__main__':
  unittest.main()