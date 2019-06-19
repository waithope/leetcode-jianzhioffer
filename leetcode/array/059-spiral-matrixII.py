## Description
## Given a positive integer n, generate a square matrix
## filled with elements from 1 to n2 in spiral order.
## Input: 3
## Output:
## [
##  [ 1, 2, 3 ],
##  [ 8, 9, 4 ],
##  [ 7, 6, 5 ]
## ]

def generateMatrix(n):
  """
  :type n: int
  :rtype: List[List[int]]
  """
  #if n == 0:
  #    return []
  #
  #matrix = [[0]*n for i in range(n)]
  #
  #rowStart, rowEnd = 0, n-1
  #colStart, colEnd = 0, n-1
  #nums = [i for i in range(1, n**2+1)]
  #ind = 0
  #while rowStart <= rowEnd and colStart <= colEnd:
  #    for i in range(colStart, colEnd+1):
  #        matrix[rowStart][i] = nums[ind]
  #        ind += 1
  #    rowStart+=1
  #
  #    for i in range(rowStart, rowEnd+1):
  #        matrix[i][colEnd] = nums[ind]
  #        ind +=1
  #    colEnd -= 1
  #
  #    if rowStart <= rowEnd:
  #        for i in range(colEnd, colStart-1, -1):
  #            matrix[rowEnd][i] = nums[ind]
  #            ind +=1
  #        rowEnd -= 1
  #    if colStart <= colEnd:
  #        for i in range(rowEnd, rowStart-1, -1):
  #            matrix[i][colStart] = nums[ind]
  #            ind +=1
  #        colStart += 1
  #
  #return matrix

## Walk the spiral path and write the numbers 1 to n*n.
## Make a turn when the cell ahead is already non-zero.
  if n == 0:
    return []

  matrix = [[0]*n for i in range(n)]
  i, j, di, dj = 0, 0, 0, 1
  for k in range(n**2):
    matrix[i][j] = k + 1
    if matrix[(i+di)%n][(j+dj)%n]:
      di, dj = dj, -di
    i += di
    j += dj
  return matrix


import unittest

class Test_Spiral_MatrixII(unittest.TestCase):
  def test_spiral_matrixii(self):
    self.assertEqual(generateMatrix(1), [[1]])
    self.assertEqual(generateMatrix(2), [[1,2],[4,3]])
    self.assertEqual(generateMatrix(3), [[1,2,3],[8,9,4],[7,6,5]])
    self.assertEqual(generateMatrix(4), [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]])


if __name__ == '__main__':
  unittest.main()