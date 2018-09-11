# Description
# Given a list of words and two words word1 and word2,
# return the shortest distance between these two words in the list.
# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
# Given word1 = “coding”, word2 = “practice”, return 3.
# Given word1 = "makes", word2 = "coding", return 1.
# Note
# You may assume that word1 does not equal to word2,
# and word1 and word2 are both in the list.


def shortestDistance(words, word1, word2):
  """
  :type words: List[str]
  :type word1: str
  :type word2: str
  :rtype: int
  """
  w1, w2 = None, None
  i, res = 0, 2**32
  while i < len(words):
    if words[i] == word1:
      w1 = i
    elif words[i] == word2:
      w2 = i
    if w1 is not None and w2 is not None:
      res = min(abs(w1-w2), res)
    i += 1
  return res




import unittest

class Test_Shortest_Distance(unittest.TestCase):
  def test_shortest_distance(self):
    self.assertEqual(shortestDistance(['practice', 'makes', 'perfect',
                                        'coding', 'makes'],'coding','practice'), 3)
    self.assertEqual(shortestDistance(['practice', 'makes', 'perfect',
                                        'coding', 'makes'],'makes','coding'), 1)


if __name__ == '__main__':
  unittest.main()
