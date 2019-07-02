
## Description
## Given a sorted integer array without duplicates,
## return the summary of its ranges.
## Input:  [0,1,2,4,5,7]
## Output: ["0->2","4->5","7"]
## Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.

## Input:  [0,2,3,4,6,8,9]
## Output: ["0","2->4","6","8->9"]
## Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.


def summaryRanges(nums):
  """
  :type nums: List[int]
  :rtype: List[str]
  """
  if nums == []:
    return []

  n = len(nums)
  l, r, res = str(nums[0]), '', []       # left and right of continuous range

  for i in range(1, n):
    if nums[i] == nums[i-1] + 1:
        continue
    else:
      r = str(nums[i-1])
      if l == r:
        res.append([l])
      else:
        res.append([l, r])
    l = str(nums[i])

  if l == str(nums[-1]):
    res.append([l])
  else:
    res.append([l, str(nums[-1])])
  return ['->'.join(item) for item in res]



import unittest
class TestSummaryRanges(unittest.TestCase):
  def test_summary_ranges(self):
    self.assertEqual(summaryRanges([0,1,2,4,5,7]), ["0->2","4->5","7"])
    self.assertEqual(summaryRanges([0,2,3,4,6,8,9]), ["0","2->4","6","8->9"])


if __name__ == '__main__':
  unittest.main()