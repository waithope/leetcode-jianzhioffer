'''
          Word Pattern
===================================
Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection
between a letter in pattern and a non-empty word in str.
Example 1:
Input: pattern = "abba", str = "dog cat cat dog"
Output: true

Example 2:
Input:pattern = "abba", str = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false

Example 4:
Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes: You may assume pattern contains only lowercase letters,
and str contains lowercase letters separated by a single space.
'''

def wordPattern(pattern, str):
  """
  :type pattern: str
  :type str: str
  :rtype: bool
  """
  #words = str.split(' ')
  #if len(pattern) != len(words):
  #    return False
  #
  #d1, d2 = {}, {}
  #for i, ch in enumerate(pattern):
  #    d1[ch] = d1.get(ch, []) + [i]
  #for i, ch in enumerate(words):
  #    d2[ch] = d2.get(ch, []) + [i]
  #return sorted(d1.values()) == sorted(d2.values())

  # words = str.split(' ')
  # return len(set(zip(pattern, words))) == len(set(pattern)) == len(set(words)) \
  #         and len(pattern) == len(words)

  words = str.split(' ')
  if len(pattern) != len(words):
    return False

  d1, d2 = {}, {}
  for i in range(len(pattern)):
    if d1.get(pattern[i], 0) != d2.get(words[i], 0):
      return False
    d1[pattern[i]] = i + 1
    d2[words[i]] = i + 1
  return True


import unittest

class Test_Word_Pattern(unittest.TestCase):
  def test_word_pattern(self):
    self.assertEqual(wordPattern('abba', 'dog cat cat dog'), True)
    self.assertEqual(wordPattern('abba', 'dog cat cat fish'), False)
    self.assertEqual(wordPattern('aaaa', 'dog cat cat dog'), False)
    self.assertEqual(wordPattern('abba', 'dog dog dog dog'), False)


if __name__ == '__main__':
  unittest.main()