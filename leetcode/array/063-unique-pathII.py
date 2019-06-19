## Description
# A robot is located at the top-left corner of
# a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid
# (marked 'Finish' in the diagram below).
# Now consider if some obstacles are added to the grids.
# How many unique paths would there be?

# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# Note: m and n will be at most 100.
# Input:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right

def uniquePathsWithObstacles(obstacleGrid):
  """
  :type obstacleGrid: List[List[int]]
  :rtype: int
  """

  m, n = len(obstacleGrid), len(obstacleGrid[0])
  path = [[0]*n for i in range(m)]

  for i in range(m):
    if obstacleGrid[i][0] == 0:
      path[i][0] = 1
    else:
      break

  for j in range(n):
    if obstacleGrid[0][j] == 0:
      path[0][j] = 1
    else:
      break

  for i in range(1, m):
    for j in range(1, n):
      if obstacleGrid[i][j]:
        path[i][j] = 0
      else:
        path[i][j] = path[i][j-1] + path[i-1][j]
  return path[-1][-1]


import unittest

class Test_Unique_PathII(unittest.TestCase):
  def test_unique_pathii(self):
    self.assertEqual(uniquePathsWithObstacles([[0]]), 1)
    self.assertEqual(uniquePathsWithObstacles([[1], [0]]), 0)
    self.assertEqual(uniquePathsWithObstacles([[0,0],[1,1],[0,0]]), 0)
    self.assertEqual(uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]), 2)


if __name__ == '__main__':
  unittest.main()