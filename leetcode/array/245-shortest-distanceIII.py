# Description
# This is a follow up of Shortest Word Distance. The only difference
# is now word1 could be the same as word2.
# Given a list of words and two words word1 and word2,
# return the shortest distance between these two words in the list.
# word1 and word2 may be the same and they represent two individual words in the list.
# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
# Given word1 = “makes”, word2 = “coding”, return 1.
# Given word1 = "makes", word2 = "makes", return 3.
# Note:
# You may assume word1 and word2 are both in the list.


def shortestWordDistance(words, word1, word2):
  """
  :type words: List[str]
  :type word1: str
  :type word2: str
  :rtype: int
  """
  # if not words:
  #   return

  # cache = {}
  # for i, word in enumerate(words):
  #   if word in cache:
  #     cache[word].append(i)
  #   else:
  #     cache[word] = [i]

  # dist = 2**32
  # if word1 == word2:
  #   dist = abs(cache[word1][0] - cache[word1][1])
  # else:
  #   w1, w2 = cache[word1], cache[word2]
  #   i, j = 0, 0
  #   while i < len(w1) and j < len(w2):
  #     dist = min(dist, abs(w1[i]-w2[j]))
  #     if w1[i] < w2[j]:
  #       i += 1
  #     else:
  #       j += 1
  # return dist

  if not words:
    return

  w1, w2, dist = -1, -1, 2**32
  for idx, word in enumerate(words):
    if word1 == word2:
      if word == word1:
        if w1 > w2:
          w2 = idx
        else: w1 = idx
    else:
      if word == word1: w1 = idx
      if word == word2: w2 = idx
    if w1 != -1 and w2 != -1:
      dist = min(dist, abs(w1 - w2))
  return dist


import unittest

class Test_Shortest_Word_Distance(unittest.TestCase):
  def test_shortest_word_distance(self):
    self.assertEqual(shortestWordDistance(['practice', 'makes', 'perfect',
                                        'coding', 'makes'],'coding','makes'), 1)
    self.assertEqual(shortestWordDistance(['practice', 'makes', 'perfect',
                                        'coding', 'makes'],'makes','makes'), 3)


if __name__ == '__main__':
  unittest.main()