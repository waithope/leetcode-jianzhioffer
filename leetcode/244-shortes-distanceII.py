# Description
# This is a follow up of Shortest Word Distance. The only difference
# is now you are given the list of words and your method will be
# called repeatedly many times with different parameters.
# How would you optimize it?

# Design a class which receives a list of words in the constructor,
# and implements a method that takes two words word1 and word2
# and return the shortest distance between these two words in the list.
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
# Given word1 = "coding”, word2 = "practice”, return 3.
# Given word1 = "makes", word2 = "coding", return 1.
# Note
# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.


def wordDistance(words, word1, word2):
  """
  :type words: List[str]
  :type word1: str
  :type word2: str
  :rtype: int
  """
  if not words:
    return

  cache = {}
  for i, word in enumerate(words):
    if word in cache:
      cache[word].append(i)
    else:
      cache[word] = [i]
  w1, w2 = cache[word1], cache[word2]
  i, j, dist = 0, 0, 2**32
  while i < len(w1) and j < len(w2):
    dist = min(dist, abs(w1[i]-w2[j]))
    if w1[i] < w2[j]:
      i += 1
    else:
      j += 1
  return dist

import unittest

class Test_Word_Distance(unittest.TestCase):
  def test_word_distance(self):
    self.assertEqual(wordDistance(['practice', 'makes', 'perfect',
                                        'coding', 'makes'],'coding','practice'), 3)
    self.assertEqual(wordDistance(['practice', 'makes', 'perfect',
                                        'coding', 'makes'],'makes','coding'), 1)


if __name__ == '__main__':
  unittest.main()