## Description
## Given a matrix of m x n elements (m rows, n columns),
## return all elements of the matrix in spiral order.
## Input:
## [
##  [ 1, 2, 3 ],
##  [ 4, 5, 6 ],
##  [ 7, 8, 9 ]
## ]
## Output: [1,2,3,6,9,8,7,4,5]
## Input:
## [
##   [1, 2, 3, 4],
##   [5, 6, 7, 8],
##   [9,10,11,12]
## ]
## Output: [1,2,3,4,8,12,11,10,9,5,6,7]

def spiralOrder(matrix):
  """
  :type matrix: List[List[int]]
  :rtype: List[int]
  """
  if not matrix:
    return []

  rowStart, rowEnd = 0, len(matrix)-1
  colStart, colEnd = 0, len(matrix[0])-1
  res = []
  while rowStart <= rowEnd and colStart <= colEnd:
    for i in range(colStart, colEnd+1):
      res.append(matrix[rowStart][i])
    rowStart += 1

    for i in range(rowStart, rowEnd+1):
      res.append(matrix[i][colEnd])
    colEnd -= 1

    if rowStart <= rowEnd:
      for i in range(colEnd, colStart-1, -1):
        res.append(matrix[rowEnd][i])
      rowEnd -= 1
    if colStart <= colEnd:
      for i in range(rowEnd, rowStart-1, -1):
        res.append(matrix[i][colStart])
      colStart += 1
  return res

  # def spiral_coords(r1, c1, r2, c2):
  #   for c in range(c1, c2+1):
  #     yield r1, c
  #   for r in range(r1+1, r2+1):
  #     yield r, c2
  #   if c1 < c2 and r1 < r2:
  #     for c in range(c2-1, c1-1, -1):
  #       yield r2, c
  #     for r in range(r2-1, r1, -1):
  #       yield r, c1

  # if not matrix:
  #     return []

  # r1, r2 = 0, len(matrix)-1
  # c1, c2 = 0, len(matrix[0])-1
  # res = []
  # while r1 <= r2 and c1 <= c2:
  #   for i, j in spiral_coords(r1, c1, r2, c2):
  #     res.append(matrix[i][j])
  #   r1 += 1
  #   r2 -= 1
  #   c1 += 1
  #   c2 -= 1
  # return res


import unittest

class Test_Spiral_Matrix(unittest.TestCase):
  def test_spiral_matrix(self):
    self.assertEqual(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]),
                                 [1,2,3,6,9,8,7,4,5])
    self.assertEqual(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]),
                                 [1,2,3,4,8,12,11,10,9,5,6,7])


if __name__ == '__main__':
  unittest.main()