## Description
## Given a non-negative integer numRows, generate the
## first numRows of Pascal's triangle. In Pascal's triangle, each number
##  is the sum of the two numbers directly above it.
## Input: 5
## Output:
## [
##      [1],
##     [1,1],
##    [1,2,1],
##   [1,3,3,1],
##  [1,4,6,4,1]
## ]


def generate(numRows):
  """
  :type numRows: int
  :rtype: List[List[int]]
  """
  #res = []
  #for i in range(numRows):
  #    if i > 1:
  #        row = [1]*(i+1)
  #        pos = 0
  #        for idx in range(1, i):
  #            row[idx] = prev[pos] + prev[pos+1]
  #            pos += 1
  #        res.append(row)
  #        prev = row
  #    else:
  #        row = [1]*(i+1)
  #        res.append(row)
  #        prev = row
  #return res

  #res = [[1]*(i+1) for i in range(numRows)]
  #for i in range(2, numRows):
  #    pos = 0
  #    prev, row = res[i-1], res[i]
  #    for idx in range(1, i):
  #        row[idx] = prev[pos] + prev[pos+1]
  #        pos += 1
  #return res

  res = [[1]*(i+1) for i in range(numRows)]
  for i in range(2, numRows):
    for j in range(1, i):
      res[i][j] = res[i-1][j-1] + res[i-1][j]
  return res


import unittest

class TestPascalTriangle(unittest.TestCase):
  def test_pascal_triangle(self):
    self.assertEqual(generate(1), [[1]])
    self.assertEqual(generate(2), [[1],[1,1]])
    self.assertEqual(generate(5), [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])
    self.assertEqual(generate(7), [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],
                                   [1,5,10,10,5,1],[1,6,15,20,15,6,1]])


if __name__ == '__main__':
  unittest.main()