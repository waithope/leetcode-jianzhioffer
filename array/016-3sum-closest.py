## Description
## Given an array nums of n integers and an integer target,
## find three integers in nums such that the sum is closest to target.
## Return the sum of the three integers.
## You may assume that each input would have exactly one solution.
## Example:
## Given array nums = [-1, 2, 1, -4], and target = 1.
## The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


def threeSumClosest(nums, target):
  """
  :type nums: List[int]
  :type target: int
  :rtype nums: int
  """
  if len(nums) < 3:
    return

  nums.sort()
  res = nums[0] + nums[1] + nums[2]
  for i in range(len(nums)-2):
    j = i + 1
    k = len(nums) - 1
    while j < k:
      s = nums[i] + nums[j] + nums[k]
      if abs(target-s) < abs(target-res):
        res = s
      if target - s == 0:
        return s
      elif target - s > 0:
        j += 1
      else:
        k -= 1
  return res


import unittest

class Test3SumClosest(unittest.TestCase):
  def test_3sum_closest(self):
    self.assertEqual(threeSumClosest([1,3,5,7], 8), 9)
    self.assertEqual(threeSumClosest([-1,2,1,-4],1), 2)
    self.assertEqual(threeSumClosest([-3,-2,-5,3,-4],-1), -2)


if __name__ == '__main__':
  unittest.main()