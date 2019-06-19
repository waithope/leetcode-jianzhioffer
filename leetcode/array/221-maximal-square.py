
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

## Time Complexity O(mn)
## Space Complexity O(n)
def maximalSquare_v2(matrix):
  if not matrix or not matrix[0]:
    return 0

  m = len(matrix)
  n = len(matrix[0])
  dp = [1 if int(x) == 1 else 0 for x in matrix[0]]
  prev = 0
  maxArea = 0 if sum(dp) == 0 else 1
  for i in range(1, m):
    for j in range(n):
      if j == 0:
        prev = dp[0]
        dp[j] = 1 if int(matrix[i][j]) == 1 else 0
      else:
        temp = dp[j]    # save previous row's state in case overriding
        dp[j] = min(prev, dp[j-1], dp[j]) + 1 if int(matrix[i][j]) == 1 else 0
        prev = temp
      maxArea = max(maxArea, dp[j])
  return maxArea**2


import unittest

class TestMaximalSquare(unittest.TestCase):
  def test_maximal_square(self):
    self.assertEqual(maximalSquare_v2([['1','0','1','0','0'],['1','0','1','1','1'],['1','1','1','1','1'],['1','0','0','1','0']]), 4)
    self.assertEqual(maximalSquare_v2([['0','1','1','1','0'],['1','1','1','1','0'],['0','1','1','1','1'],['0','1','1','1','1'],['0','0','1','1','1']]), 9)


if __name__ == '__main__':
  unittest.main()