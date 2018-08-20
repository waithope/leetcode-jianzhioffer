## Description
## Given a triangle, find the minimum path sum from top to bottom.
## Each step you may move to adjacent numbers on the row below.
## For example, given the following triangle
## [
##      [2],
##     [3,4],
##    [6,5,7],
##   [4,1,8,3]
## ]
## The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
## Bonus point if you are able to do this using only O(n) extra space


def minimumTotal(triangle):
  """
  :type triangle: List[List[int]]
  :rtype: int
  """
  ## Top-down   modifying the original triangle
  # if not triangle:
  #   return

  # for i in range(1, len(triangle)):
  #   for j in range(i+1):
  #     if j == 0:
  #       triangle[i][j] = triangle[i][j] + triangle[i-1][j]
  #     elif j == i:       # i is len(triangle[i]) - 1
  #       triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
  #     else:
  #       triangle[i][j] = min(triangle[i-1][j-1], triangle[i-1][j]) + triangle[i][j]
  # return min(triangle[-1])

  ## Bottom-up  O(N) space without modifying the original triangle
  if not triangle:
    return

  layers = len(triangle)
  minpath = list(triangle[-1])     # avoiding modification to original list due to reference
  for k in range(layers-2, -1, -1):
    for i in range(k+1):           # compute minimum path of ith node in k layers
      minpath[i] = min(minpath[i], minpath[i+1]) + triangle[k][i]
  return minpath[0]


import unittest

class TestTriangle(unittest.TestCase):
  def test_triangle(self):
    self.assertEqual(minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]), 11)

if __name__ == '__main__':
  unittest.main()