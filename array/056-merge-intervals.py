## Description
## Given a collection of intervals, merge all overlapping intervals.
## Input: [[1,3],[2,6],[8,10],[15,18]]
## Output: [[1,6],[8,10],[15,18]]
## Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
#
## Input: [[1,4],[4,5]]
## Output: [[1,5]]
## Explanation: Intervals [1,4] and [4,5] are considerred overlapping.


def merge(intervals):
  """
  :type intervals: List[Interval]
  :rtype: List[Interval]
  """
  intervals.sort(key=lambda x:x[0])

  merged = []
  for interval in intervals:
      if not merged or merged[-1][-1] < interval[0]:
          merged.append(interval)
      else:
          merged[-1][-1] = max(merged[-1][-1], interval[-1])

  return merged


import unittest

class Test_Merge_Intervals(unittest.TestCase):
  def test_merge_intervals(self):
    self.assertEqual(merge([[1,4],[4,5]]), [[1,5]])
    self.assertEqual(merge([[1,4],[2,3],[4,10]]), [[1,10]])
    self.assertEqual(merge([[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]])


if __name__ == '__main__':
  unittest.main()