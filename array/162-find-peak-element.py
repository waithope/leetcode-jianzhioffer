## Description
## A peak element is an element that is greater than its neighbors.
## Given an input array nums, where nums[i] ≠ nums[i+1],
## find a peak element and return its index.
## The array may contain multiple peaks,
## in that case return the index to any one of the peaks is fine.
## You may imagine that nums[-1] = nums[n] = -∞.

## Input: nums = [1,2,3,1]
## Output: 2
## Explanation: 3 is a peak element and your function should return the index number 2.
## Input: nums = [1,2,1,3,5,6,4]
## Output: 1 or 5
## Explanation: Your function can return either index number 1
## where the peak element is 2,or index number 5 where the peak element is 6.

## Binary Search Method
## We start off by finding the middle element, mid from the given numsnums array.
## If this element happens to be lying in a descending sequence of numbers.
## or a local falling slope(found by comparing nums[i] to its right neighbour),
## it means that the peak will always lie towards the left of this element.
## Thus, we reduce the search space to the left of midmid(including itself)
## and perform the same process on left subarray.
## If the middle element, mid lies in an ascending sequence of numbers,
## or a rising slope(found by comparing nums[i]nums[i] to its right neighbour),
## it obviously implies that the peak lies towards the right of this element.
## Thus, we reduce the search space to the right of mid
## and perform the same process on the right subarray.


def findPeakElement(nums):
  """
  :type nums: List[int]
  :rtype: int
  """

  left, right = 0, len(nums) - 1

  while left < right:
    mid = left + (right-left) // 2
    if nums[mid] > nums[mid+1]:
      right = mid
    else:
      left = mid + 1
  return left


import unittest

class TestFindPeakElement(unittest.TestCase):
  def test_peak_element(self):
    self.assertEqual(findPeakElement([1,2,3,1]), 2)
    self.assertEqual(findPeakElement([1,2,1,3,5,6,4]), 5)


if __name__ == '__main__':
  unittest.main()
