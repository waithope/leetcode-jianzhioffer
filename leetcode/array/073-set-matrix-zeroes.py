# Description
# Given a m x n matrix, if an element is 0,
# set its entire row and column to 0. Do it in-place.
# Example 1:
# Input:
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# Output:
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
# Example 2:
# Input:
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# Output:
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
# Follow up:

# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?

def setZeroes(matrix):
  """
  :type matrix: List[List[int]]
  :rtype: void Do not return anything, modify matrix in-place instead.
  """
  # O(m*n) space
  #if not matrix:
  #    return
  #
  #m, n = len(matrix), len(matrix[0])
  #ind = [[], []]
  #for i in range(m):
  #    for j in range(n):
  #        if matrix[i][j] == 0:
  #            ind[0].append(i)
  #            ind[1].append(j)
  #for i in range(len(ind)):
  #
  #for i in range(m):
  #    for j in range(n):
  #        if i in ind[0] or j in ind[1]:
  #            matrix[i][j] = 0

  # O(1) space
  if not matrix:
    return

  col0, rows, cols = 1, len(matrix), len(matrix[0])
  for i in range(rows):
    if matrix[i][0] == 0: col0 = 0
    for j in range(1, cols):  # using the firt row and first col to save states
      if matrix[i][j] == 0:
        matrix[i][0] = matrix[0][j] = 0

  for i in range(rows)[::-1]:
    for j in range(1, cols)[::-1]:
      if matrix[i][0] == 0 or matrix[0][j] == 0:
        matrix[i][j] = 0
    if col0 == 0: matrix[i][0] =0
  return matrix


import unittest

class Test_Set_Matrix_Zeroes(unittest.TestCase):
  def test_set_matrix_zeroes(self):
    self.assertEqual(setZeroes([[1,1,1],[1,0,1],[1,1,1]]),
                               [[1,0,1],[0,0,0],[1,0,1]])
    self.assertEqual(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]),
                               [[0,0,0,0],[0,4,5,0],[0,3,1,0]])

if __name__ == '__main__':
  unittest.main()