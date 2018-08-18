## Description
## Given an array nums, write a function to move all 0's to the end of it
## while maintaining the relative order of the non-zero elements.
## Input: [0,1,0,3,12]
## Output: [1,3,12,0,0]
## You must do this in-place without making a copy of the array.

def moveZeroes(nums):
  """
  :type nums: List[int]
  :rtype: void Do not return anything, modify nums in-place instead.
  """

  #head, tail = -1, 0
  #while tail < len(nums):
  #    if nums[tail] == 0 and head == -1:
  #        head = tail
  #    elif head != -1 and nums[tail] != 0:
  #        nums[head], nums[tail] = nums[tail], nums[head]
  #        head += 1
  #    tail += 1

  #tail = 0
  #for i in range(len(nums)):
  #    if nums[i] != 0:
  #        nums[i], nums[tail] = nums[tail], nums[i]
  #        tail += 1

  tail = 0
  for num in nums:
    if num != 0:
      nums[tail] = num
      tail += 1
  for i in range(tail, len(nums)):
    nums[i] = 0
  return nums


import unittest

class TestMoveZeroes(unittest.TestCase):
  def test_move_zeroes(self):
    self.assertEqual(moveZeroes([0]), [0])
    self.assertEqual(moveZeroes([1,2]), [1,2])
    self.assertEqual(moveZeroes([0,1,0,3,12]), [1,3,12,0,0])
    self.assertEqual(moveZeroes([4,2,3,1,0,0,5,1]), [4,2,3,1,5,1,0,0])


if __name__ == '__main__':
  unittest.main()