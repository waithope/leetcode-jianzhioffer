
## Description
## Given an integer array of size n, find all elements that
## appear more than ⌊ n/3 ⌋ times.
## Input: [3,2,3]
## Output: [3]
## Input: [1,1,1,3,3,2,2,2]
## Output: [1,2]

## Time O(n) Space O(1)
def majorityElement(nums):
  """
  :type nums: List[int]
  :rtype: List[int]
  """
  if nums == []:
    return []

  n = len(nums)
  nums.sort()
  res, th, cnt, curr = [], n//3, 1, nums[0]
  for i in range(n-1):
    if curr == nums[i+1]:
      cnt += 1
      continue
    else:
      if cnt > th:
        res.append(curr)
      cnt, curr = 1, nums[i+1]
  if cnt > th:
    res.append(curr)
  return res


import unittest

class TestMajorityElementsII(unittest.TestCase):
  def test_majority_elementsII(self):
    self.assertEqual(majorityElement([1,2]), [1,2])
    self.assertEqual(majorityElement([3,2,3]), [3])
    self.assertEqual(majorityElement([1,1,1,3,3,2,2,2]), [1,2])


if __name__ == '__main__':
  unittest.main()