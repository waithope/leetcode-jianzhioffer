# Description
# Given a m x n grid filled with non-negative numbers,
# find a path from top left to bottom right
# which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.
# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.

def minPathSum(grid):
  """
  :type grid: List[List[int]]
  :rtype: int
  """
  # O(m*n) space
  #if not grid:
  #    return

  #m, n = len(grid), len(grid[0])
  #path = [[0]*(n) for i in range(m)]
  #
  #path[0][0] = grid[0][0]
  #for i in range(1, m):
  #    path[i][0] = path[i-1][0] + grid[i][0]
  #for j in range(1, n):
  #    path[0][j] = path[0][j-1] + grid[0][j]
  #
  #for i in range(1, m):
  #    for j in range(1, n):
  #        path[i][j] = min(path[i-1][j], path[i][j-1]) + grid[i][j]
  #return path[-1][-1]

  # O(n) space
  if not grid:
    return

  m, n = len(grid), len(grid[0])
  dp = [0]*n
  dp[0] = grid[0][0]
  for i in range(1, n):
    dp[i] = dp[i-1] + grid[0][i]

  for i in range(1, m):
    dp[0] += grid[i][0]
    for j in range(1, n):
      dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
  return dp[-1]


import unittest

class Test_Minimum_Path_Sum(unittest.TestCase):
  def test_minimum_path_sum(self):
    self.assertEqual(minPathSum([[2,6],[3,1],[3,1]]), 7)
    self.assertEqual(minPathSum([[1,3,1],[1,5,1],[4,2,1]]), 7)

if __name__ == '__main__':
  unittest.main()

