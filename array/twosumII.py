## Description
## Given an array of integers that is already sorted in ascending order,
## find two numbers such that they add up to a specific target number.
## The function twoSum should return indices of the two numbers
## such that they add up to the target, where index1 must be less than index2.
## Note:
## Your returned answers (both index1 and index2) are not zero-based.
## You may assume that each input would have exactly one solution
## and you may not use the same element twice.

## Input: numbers = [2,7,11,15], target = 9
## Output: [1,2]
## Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

def twoSum(numbers, target):
  """
  :type numbers: List[int]
  :type target: int
  :rtype: List[int]
  """
  #left, right = 0, len(numbers) - 1
  #while left < right:
  #    curSum = numbers[left] + numbers[right]
  #    if curSum == target:
  #        return [left + 1, right + 1]
  #    elif curSum < target:
  #        left += 1
  #    else:
  #        right -= 1
  c = {}
  for idx, num in enumerate(numbers, 1):
    if num in c:
      return [c[num], idx]
    c[target-num] = idx
  return []

import unittest

class TestTwoSumII(unittest.TestCase):
  def test_two_sumII(self):
    self.assertEqual(twoSum([2,7,11,15], 9), [1, 2])
    self.assertEqual(twoSum([2,8,13,33,23,14], 36), [3, 5])
    self.assertEqual(twoSum([5,8,13,33,23,14], 19), [1, 6])


if __name__ == '__main__':
  unittest.main()