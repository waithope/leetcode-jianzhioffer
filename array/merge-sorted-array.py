## Description
## Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1
## as one sorted array.
## Note:
## The number of elements initialized in nums1 and nums2 are m and n respectively.
## You may assume that nums1 has enough space (size that is greater
## or equal to m + n) to hold additional elements from nums2.
## Input:
## nums1 = [1,2,3,0,0,0], m = 3
## nums2 = [2,5,6],       n = 3
## Output: [1,2,2,3,5,6]

def merge(nums1, m, nums2, n):
  """
  :type nums1: List[int]
  :type m: int
  :type nums2: List[int]
  :type n: int
  :rtype: void Do not return anything, modify nums1 in-place instead.
  """
  #for i in range(n):
  #    idx = m + i
  #    nums1[idx] = nums2[i]
  #nums1.sort()
  while m > 0 and n > 0:
    if nums1[m-1] > nums2[n-1]:
      nums1[m+n-1] = nums1[m-1]
      m -= 1
    else:
      nums1[m+n-1] = nums2[n-1]
      n -= 1
  if n > 0:
    nums1[:n] = nums2[:n]
  return nums1


import unittest

class TestMerge(unittest.TestCase):
  def test_merge(self):
    self.assertEqual(merge([1,2,3,0,0,0],3,[2,5,6],3), [1,2,2,3,5,6])
    self.assertEqual(merge([1,2,3,8,9,0,0,0],5,[2,5,6],3), [1,2,2,3,5,6,8,9])
    self.assertEqual(merge([1,4,6,8,9,0,0,0,0,0],5,[2,5,6,7,10],5), [1,2,4,5,6,6,7,8,9,10])


if __name__ == '__main__':
  unittest.main()