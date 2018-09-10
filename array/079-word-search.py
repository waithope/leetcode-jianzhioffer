# Description
# Given a 2D board and a word, find if the word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring
# (It means you can search letter in right or left or up or down at most 1 grid).
# The same letter cell may not be used more than once.

# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.


def exist(board, word):
  """
  :type board: List[List[str]]
  :type word: str
  :rtype: bool
  """
  def exist(matrix, x, y, string, start):
    if start >= len(string):
      return True
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
      return False
    if matrix[x][y] == string[start]:
      start += 1
      c = matrix[x][y]
      matrix[x][y] = '#'
      # search letter at position of left, right, up, down
      res = exist(matrix, x-1, y, string, start) \
        or exist(matrix, x+1, y, string, start) \
        or exist(matrix, x, y-1, string, start) \
        or exist(matrix, x, y+1, string, start)
      matrix[x][y] = c
      return res
    return False

  for i in range(len(board)):
    for j in range(len(board[0])):
      if exist(board, i, j, word, 0):
        return True
  return False


import unittest

class Test_Word_Search(unittest.TestCase):
  def test_word_search(self):
    self.assertEqual(exist([['A','B','C','E'],
                            ['S','F','C','S'],
                            ['A','D','E','E']], 'ABCCED'), True)
    self.assertEqual(exist([['A','B','C','E'],
                            ['S','F','C','S'],
                            ['A','D','E','E']], 'SEE'), True)
    self.assertEqual(exist([['A','B','C','E'],
                            ['S','F','C','S'],
                            ['A','D','E','E']], 'ABCB'), False)

if __name__ == '__main__':
  unittest.main()