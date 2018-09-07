## Description
# A robot is located at the top-left corner of
# a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid
# (marked 'Finish' in the diagram below).
# How many possible unique paths are there?

# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways
# to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right

# Input: m = 7, n = 3
# Output: 28


def uniquePaths(m, n):
  """
  :type m: int
  :type n: int
  :rtype: int
  """
  ## time complexity O(n**2) space complexity O(m*n)
  #path = [[1]*n for i in range(m)]
  #
  #for i in range(1, m):
  #    for j in range(1, n):
  #        path[i][j] = path[i-1][j] + path[i][j-1]
  #return path[m-1][n-1]

  ## time complexity O(n**2) space complexity O(n)
  dp = [1]*n
  for i in range(1, m):
      for j in range(1, n):
          dp[j] = dp[j-1] + dp[j]
  return dp[-1]


import unittest

class Test_Unique_Path(unittest.TestCase):
  def test_unique_path(self):
    self.assertEqual(uniquePaths(3, 2), 3)
    self.assertEqual(uniquePaths(7, 3), 28)


if __name__ == '__main__':
  unittest.main()

