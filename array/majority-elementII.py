
## Description
## Given an integer array of size n, find all elements that
## appear more than ⌊ n/3 ⌋ times.
## Input: [3,2,3]
## Output: [3]
## Input: [1,1,1,3,3,2,2,2]
## Output: [1,2]

## Time O(nlog(n)) Space O(1)
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


## Boyer–Moore majority vote algorithm
## Time O(n) Space O(1)
def majorityElement_v2(nums):
  if nums == []:
    return []

  candidate1, candidate2, cnt1, cnt2 = None, None, 0, 0
  for num in nums:
    if num == candidate1:
      cnt1 += 1
    elif num == candidate2:
      cnt2 += 1
    elif cnt1 == 0:
      cnt1 = 1
      candidate1 = num
    elif cnt2 == 0:
      cnt2 = 1
      candidate2 = num
    else:
      cnt1 -= 1
      cnt2 -= 1
  return [x for x in (candidate1, candidate2) if nums.count(x) > len(nums)//3]

import unittest

class TestMajorityElementsII(unittest.TestCase):
  def test_majority_elementsII(self):
    self.assertEqual(majorityElement_v2([0,0,0]), [0])
    self.assertEqual(majorityElement_v2([1,2]), [1,2])
    self.assertEqual(majorityElement_v2([3,2,3]), [3])
    self.assertEqual(majorityElement_v2([1,1,1,3,3,2,2,2]), [1,2])


if __name__ == '__main__':
  unittest.main()