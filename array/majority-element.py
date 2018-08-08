## Description
## Given an integer array of size n, find all elements that
## appear more than ⌊ n/2 ⌋ times.
## You may assume that the array is non-empty and
## the majority element always exist in the array.
## Input: [3,2,3]
## Output: 3
## Input: [2,2,1,1,1,2,2]
## Output: 2

def majorityElement(nums):
  """
  :type nums: List[int]
  :rtype: int
  """
  if nums == []:
    return []

  candidate, count = None, 0
  for num in nums:
    if count == 0:
      candidate = num
      count += 1
    elif num == candidate:
      count += 1
    else:
      count -= 1
  return candidate


import unittest

class TestMajorityElement(unittest.TestCase):
  def test_majority_element(self):
    self.assertEqual(majorityElement([1,2,1]), 1)
    self.assertEqual(majorityElement([3,2,3]), 3)
    self.assertEqual(majorityElement([0,0,0]), 0)
    self.assertEqual(majorityElement([1,2,1,3,1]), 1)
    self.assertEqual(majorityElement([1,1,1,3,1,3,2,2,2,1,1]), 1)
    self.assertEqual(majorityElement([2,2,1,1,1,2,2]), 2)


if __name__ == '__main__':
  unittest.main()