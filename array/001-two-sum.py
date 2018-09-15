'''
 Given an array of integers, return indices of the two numbers
 such that they add up to a specific target.
 You may assume that each input would have exactly one solution,
 and you may not use the same element twice.
 Given nums = [2, 7, 11, 15], target = 9,
 Because nums[0] + nums[1] = 2 + 7 = 9,
 return [0, 1].
'''

def twoSum(nums, target):
  """
  :type nums: List[int]
  :type target: int
  :rtype: List[int]
  """
  #n = len(nums)
  #if n < 2:
  #    return []
  #res = []
  #for i in range(n-1):
  #    j = i + 1
  #    while j < n:
  #        s = nums[i] + nums[j]
  #        if s == target:
  #            return [i, j]
  #        else:
  #            j += 1

  c = {}
  for idx, num in enumerate(nums):
    if num in c:
        return [c[num], idx]
    c[target-num] = idx
  return []



import unittest

class TestTwoSum(unittest.TestCase):
  def test_two_sum(self):
    self.assertEqual(twoSum([2,7,11,15], 9), [0, 1])
    self.assertEqual(twoSum([2,8,13,33,23,14], 36), [2, 4])
    self.assertEqual(twoSum([5,8,13,33,23,14], 19), [0, 5])


if __name__ == '__main__':
  unittest.main()