'''
      Palindrome Permutation
===================================
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:
Input: "code"
Output: false

Example 2:
Input: "aab"
Output: true

Example 3:
Input: "carerac"
Output: true
'''

def canPermutePalindrome(s):
  count, res = {}, 0
  for ch in s:
    count[ch] = count.get(ch, 0) + 1
  for val in count.values():
    res += (val%2)
  return res < 2


import unittest

class Test_Palindrome_Permuatation(unittest.TestCase):
  def test_palindrome_permutation(self):
    self.assertEqual(canPermutePalindrome('code'), False)
    self.assertEqual(canPermutePalindrome('aab'), True)
    self.assertEqual(canPermutePalindrome('carerac'), True)

if __name__ == '__main__':
  unittest.main()