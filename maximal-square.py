
## Description
## Given a 2D binary matrix filled with 0's and 1's,
## find the largest square containing only 1's and return its area.
# Input:

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0

# Output: 4

## Time Complexity O(mn)
## Space Complexity O(mn)
def maximalSquare(matrix):
  if not matrix or not matrix[0]:
    return 0

  m = len(matrix)
  n = len(matrix[0])
  maxArea = 0
  dp = [[0]*n for _ in range(m)]
  for i in range(m):
    for j in range(n):
      if i == 0 or j == 0:
        dp[i][j] = int(matrix[i][j])
      elif int(matrix[i][j]) == 1:
        dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
      maxArea = max(maxArea, dp[i][j])
  return maxArea**2


import unittest

class TestMaximalSquare(unittest.TestCase):
  def test_maximal_square(self):
    self.assertEqual(maximalSquare([['1','0','1','0','0'],['1','0','1','1','1'],['1','1','1','1','1'],['1','0','0','1','0']]), 4)
    self.assertEqual(maximalSquare([['0','1','1','1','0'],['1','1','1','1','0'],['0','1','1','1','1'],['0','1','1','1','1'],['0','0','1','1','1']]), 9)


if __name__ == '__main__':
  unittest.main()