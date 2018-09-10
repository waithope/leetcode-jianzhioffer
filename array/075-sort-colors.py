# Description
# Given an array with n objects colored red, white or blue,
# sort them in-place so that objects of the same color are adjacent,
# with the colors in the order red, white and blue.
# Here, we will use the integers 0, 1, and 2 to represent the color
# red, white, and blue respectively.
# Note: You are not suppose to use the library's sort function for this problem.
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Follow up:
# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's,
# then overwrite array with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?


def sortColors(nums):
  """
  :type nums: List[int]
  :rtype: void Do not return anything, modify nums in-place instead.
  """
  #def partition(nums, l, h, li, mj):
  #    if h-l <= 1:
  #        if nums[h] < nums[l]:
  #            nums[h], nums[l] = nums[l], nums[h]
  #            l += 1
  #            h -= 1
  #        li = l
  #        mj = h
  #
  #    pivot = nums[h]
  #    li = l
  #    mj = l
  #    while mj <= h:
  #        if nums[mj] < pivot:
  #            nums[mj], nums[li] = nums[li], nums[mj]
  #            li += 1
  #            mj += 1
  #        elif nums[mj] == pivot:
  #            mj += 1
  #        else:
  #            nums[mj], nums[h] = nums[h], nums[mj]
  #            h -= 1
  #    return li-1, mj
  #def quicksort(nums, l, h):
  #    li, mj = None, None
  #    if l < h:
  #        li, mj = partition(nums, l, h, li, mj)
  #        quicksort(nums, l, li)
  #        quicksort(nums, mj, h)
  #
  #
  #l, h = 0, len(nums)-1
  #quicksort(nums, l, h)

  l, h = 0, len(nums)-1
  for i in range(len(nums)):
    while i < h and nums[i] == 2:
      nums[i], nums[h] = nums[h], nums[i]
      h -= 1
    while l < i and nums[i] == 0:
      nums[i], nums[l] = nums[l], nums[i]
      l += 1
  return nums

import unittest

class Test_Sort_Colors(unittest.TestCase):
  def test_sort_colors(self):
    self.assertEqual(sortColors([1,0,2]), [0,1,2])
    self.assertEqual(sortColors([2,0,2,1,1,0]), [0,0,1,1,2,2])

if __name__ == '__main__':
  unittest.main()