# Description
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# Example 1:

# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# Output: true
# Example 2:

# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# Output: false

def searchMatrix(matrix, target):
  """
  :type matrix: List[List[int]]
  :type target: int
  :rtype: bool
  """
  # time complexity O(m*log(n))
  #def binarySearch(nums, target):
  #    if not nums:
  #        return False
  #    left, right = 0, len(nums)-1
  #    while left < right:
  #        mid = left + (right - left) // 2
  #        if nums[mid] == target:
  #            return True
  #        elif nums[mid] < target:
  #            left = mid + 1
  #        else:
  #            right = mid - 1
  #    if nums[left] == target:
  #        return True
  #    return False
  #
  #if not matrix:
  #    return False
  #
  #for i in range(len(matrix)):
  #    if binarySearch(matrix[i], target):
  #        return True
  #return False

  # time complexity O(log(m*n))
  if not matrix:
    return False
  m, n = len(matrix), len(matrix[0])
  start, end = 0, m*n-1

  while start <= end:
    mid = start + (end - start) // 2
    rows, cols =  mid // n, mid % n
    if matrix[rows][cols] == target:
      return True
    elif matrix[rows][cols] < target:
      start = mid + 1
    else:
      end = mid - 1
  return False


import unittest

class Test_Search_2D_Matrix(unittest.TestCase):
  def test_search_2d_matrix(self):
    self.assertEqual(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],3),True)
    self.assertEqual(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],13),False)


if __name__ == '__main__':
  unittest.main()