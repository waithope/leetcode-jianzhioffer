
## Description
## Given string S and a dictionary of words words,
## find the number of words[i] that is a subsequence of S

## Example :
## Input:
## S = "abcde"
## words = ["a", "bb", "acd", "ace"]
## Output: 3
## Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".

import collections
def numMatchingSubseq(S, words):
  """
  :type S: str
  :type words: List[str]
  :rtype: int
  """
  waiting = collections.defaultdict(list)  # set dict default keyvalue is list []
  for w in words:
    waiting[w[0]].append(iter(w[1:]))     # append subsequent iterator

  for ch in S:
    for iter_ in waiting.pop(ch, ()):
      waiting[next(iter_, None)].append(iter_)
  return len(waiting[None])


import unittest

class TestNumMatchingSubseq(unittest.TestCase):
  def test_num_matching_subseq(self):
    self.assertEqual(numMatchingSubseq('abcde', ['a', 'bb', 'acd', 'ace']), 3)
    self.assertEqual(numMatchingSubseq('dfdafdsa', ['dd', 'ab', 'afa', 'cd']), 2)


if __name__ == '__main__':
  unittest.main()