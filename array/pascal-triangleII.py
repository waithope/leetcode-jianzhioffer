## Description
## Given a non-negative index k where k ≤ 33,
## return the kth index row of the Pascal's triangle.
## Note that the row index starts from 0.
## Input: 3
## Output: [1,3,3,1]
## Optimize your algorithm to use only O(k) extra space

def getRow(rowIndex):
  """
  :type rowIndex: int
  :rtype: List[int]
  """
  #prev = []
  #for i in range(rowIndex+1):
  #    if i < 2:
  #        prev = [1]*(i+1)
  #    else:
  #        row = [1]*(i+1)
  #        for j in range(1, i):
  #            row[j] = prev[j-1] + prev[j]
  #        prev = row
  #return prev

  l = [1]
  for i in range(1, rowIndex+1):
    last = 1
    for j in range(1, i):
      aux = l[j]
      l[j] = l[j] + last
      last = aux
    l.append(1)
  return l


import unittest

class TestPascalTriangleII(unittest.TestCase):
  def test_pascal_triangleII(self):
    self.assertEqual(getRow(0), [1])
    self.assertEqual(getRow(1), [1,1])
    self.assertEqual(getRow(3), [1,3,3,1])
    self.assertEqual(getRow(4), [1,4,6,4,1])
    self.assertEqual(getRow(5), [1,5,10,10,5,1])
    self.assertEqual(getRow(6), [1,6,15,20,15,6,1])


if __name__ == '__main__':
  unittest.main()

