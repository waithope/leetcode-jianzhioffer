'''
          Valid Anagram
===================================
Given two strings s and t , write a function to determine if t is an anagram of s.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Note: You may assume the string contains only lowercase alphabets.
'''

def isAnagram(s, t):
  """
  :type s: str
  :type t: str
  :rtype: bool
  """
  #if len(s) != len(t):
  #    return False
  #return sorted(s) == sorted(t)

  if len(s) != len(t):
    return False

  count = [0] * 26
  for i in range(len(s)):
    count[ord(s[i]) - ord('a')] += 1
    count[ord(t[i]) - ord('a')] -= 1

  return [0]*26 == count


import unittest

class Test_Valid_Anagram(unittest.TestCase):
  def test_valid_anagram(self):
    self.assertEqual(isAnagram('cat', 'car'), False)
    self.assertEqual(isAnagram('anagram', 'nagaram'), True)


if __name__ == '__main__':
  unittest.main()