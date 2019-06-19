'''
        Next Permutation
==================================
Implement next permutation, which rearranges numbers
into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it
as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.
Here are some examples. Inputs are in the left-hand column
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
(1, 2, 3, 4, 5)
(1, 2, 3, 5, 4)
(1, 2, 4, 3, 5)
(1, 2, 4, 5, 3)
(1, 2, 5, 3, 4)
(1, 2, 5, 4, 3)
(1, 3, 2, 4, 5)
(1, 3, 2, 5, 4)
(1, 3, 4, 2, 5)
(1, 3, 4, 5, 2)
(1, 3, 5, 2, 4)
(1, 3, 5, 4, 2)
(1, 4, 2, 3, 5)
(1, 4, 2, 5, 3)
(1, 4, 3, 2, 5)
(1, 4, 3, 5, 2)
(1, 4, 5, 2, 3)
(1, 4, 5, 3, 2)
(1, 5, 2, 3, 4)
(1, 5, 2, 4, 3)
(1, 5, 3, 2, 4)
(1, 5, 3, 4, 2)
(1, 5, 4, 2, 3)
(1, 5, 4, 3, 2)
For any given sequence that is in descending order,
no next larger permutation is possible, return it's reversed list
next, need to find the first pair of two successive numbers a[i]
and a[i−1], from the right, which satisfy a[i] > a[i-1].
then, replace the number a[i-1] with the number which is just
larger than itself among the numbers lying to its right section, say a[j].
swap the numbers a[i-1] and a[j], We need the smallest permutation that
can be formed by using the numbers only to the right of a[i-1].
Therefore, we need to place those numbers in ascending order to
get their smallest permutation
'''

def nextPermutation(nums):
  """
  :type nums: List[int]
  :rtype: void Do not return anything, modify nums in-place instead.
  """
  def reverse(start):
    end = len(nums) - 1
    while start < end:
      nums[start], nums[end] = nums[end], nums[start]
      start += 1
      end -= 1

  if not nums:
    return []

  i = len(nums) - 2
  while i >= 0 and nums[i+1] <= nums[i]:
    i -= 1

  j = len(nums) - 1
  while j >= 0 and nums[j] <= nums[i]:
    j -= 1

  if i >= 0:
    nums[i], nums[j] = nums[j], nums[i]
    reverse(i+1)
  else:
    reverse(0)
  return nums


import unittest

class TestNextPermutation(unittest.TestCase):
  def test_next_permutation(self):
    self.assertEqual(nextPermutation([1,2,3]), [1,3,2])
    self.assertEqual(nextPermutation([3,2,1]), [1,2,3])
    self.assertEqual(nextPermutation([1,1,5]), [1,5,1])
    self.assertEqual(nextPermutation([1,4,5,3,2]), [1,5,2,3,4])


if __name__ == '__main__':
  unittest.main()