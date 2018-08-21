## Description
## Given a sorted integer array where the range of elements are [0, 99] inclusive,
## return its missing ranges. For example, given [0, 1, 3, 50, 75],
## return [“2”, “4->49”, “51->74”, “76->99”]
## Example Questions:
## if the given array is empty, then you should return [“0->99”]
## as those ranges are missing.
## if the given array contains all elements from the ranges
## then return an empty list, which means no range is missing.
## Explanation:
## Compare the gap between two neighbor elements and output its range,
## This seems deceptively easy, except there are multiple edge cases to consider,
## such as the first and last element, which does not have previous and next element.
## Also, what happens when the given array is empty? We should output the range “0->99”.
## As it turns out, if we could add two “artificial” elements, –1 before the first element
## and 100 after the last element, we could avoid all the above pesky cases.


def missingRanges(nums, start, end):
  """
  :type nums: List[int]
  :type lower: int
  :type upper: int
  :rtype: List[str]
  """
  def getRange(lower, upper):
    if lower == upper:
      return '{}'.format(lower)
    else:
      return '{}->{}'.format(lower, upper)

  n = len(nums)
  ranges, pre = [], start-1
  for i in range(n+1):
    if i == n:
      cur = end + 1
    else:
      cur = nums[i]

    if cur - pre >= 2:
      ranges.append(getRange(pre+1, cur-1))
    pre = cur
  return ranges


import unittest

class TestMissingRanges(unittest.TestCase):
  def test_missing_ranges(self):
    self.assertEqual(missingRanges([0,0,20], 0, 30), ['1->19', '21->30'])
    self.assertEqual(missingRanges([97,99], 0, 99), ['0->96', '98'])
    self.assertEqual(missingRanges([0,1,3,50,75], 0, 99), ['2','4->49', '51->74', '76->99'])
    self.assertEqual(missingRanges([0,2,3,10,88,400], 0, 999),
                                   ['1','4->9','11->87','89->399','401->999'])


if __name__ == '__main__':
  unittest.main()
