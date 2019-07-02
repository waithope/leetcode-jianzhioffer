## Description
## Given an array, rotate the array to the right by k steps,
## where k is non-negative.
## Input: [1,2,3,4,5,6,7] and k = 3
## Output: [5,6,7,1,2,3,4]
## Explanation:
## rotate 1 steps to the right: [7,1,2,3,4,5,6]
## rotate 2 steps to the right: [6,7,1,2,3,4,5]
## rotate 3 steps to the right: [5,6,7,1,2,3,4]
## do it in-place with O(1) extra space

def rotate(nums, k):
  """
  :type nums: List[int]
  :type k: int
  :rtype: void Do not return anything, modify nums in-place instead.
  """

  #for i in range(k):
  #    temp = nums.pop()
  #    nums.insert(0, temp)

  n = len(nums)
  k = k % n
  nums[:] = nums[n-k:] + nums[:n-k]
  return nums


import unittest

class TestRotateArray(unittest.TestCase):
  def test_rotate_array(self):
    self.assertEqual(rotate([1], 3), [1])
    self.assertEqual(rotate([1,2], 3), [2,1])
    self.assertEqual(rotate([-1,-100,3,99], 2), [3,99,-1,-100])
    self.assertEqual(rotate([1,2,3,4,5,6,7], 3), [5,6,7,1,2,3,4])

if __name__ == '__main__':
  unittest.main()



