## Desciption
## Suppose an array sorted in ascending order is rotated
## at some pivot unknown to you beforehand.
## (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
## Find the minimum element.
## You may assume no duplicate exists in the array.
## Input: [3,4,5,1,2]
## Output: 1
## Input: [4,5,6,7,0,1,2]
## Output: 0

def findMin(nums):
  """
  :type nums: List[int]
  :rtype: int
  """
  #left, right = 0, len(nums)-1
  #
  #while left <= right:
  #    mid = (left + right) // 2
  #    if nums[left] <= nums[mid] <= nums[right]:
  #        return nums[left]
  #    elif nums[mid] > nums[right]:
  #        left = mid + 1
  #    elif nums[mid] < nums [right]:
  #        right = mid

  left, right = 0, len(nums)-1

  while left < right:
    if nums[left] < nums[right]:
      return nums[left]
    mid = (left + right) // 2     # avoiding operation overflow
    if nums[mid] >= nums[left]:
      left = mid + 1
    else:
      right = mid

  return nums[left]


import unittest

class TestFindMinimum(unittest.TestCase):
  def test_find_minimum(self):
    self.assertEqual(findMin([1]), 1)
    self.assertEqual(findMin([3,1,2]), 1)
    self.assertEqual(findMin([3,4,5,1,2]), 1)
    self.assertEqual(findMin([4,5,6,7,0,1,2]), 0)
    self.assertEqual(findMin([3,4,5,6,7,8,9,0,1,2]), 0)


if __name__ == '__main__':
  unittest.main()