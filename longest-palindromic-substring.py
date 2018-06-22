
## Description
## Given a string s, find the longest palindromic substring in s.
## Input: "babad"
## Output: "bab"
## Note: "aba" is also a valid answer.

## Dynamic Programming  O(N^2) with O(N) space
def longestPalindrome(s):
  size = len(s)
  dp = [[False]*size, [False]*size]
  max_i, max_j, max_len = 0, 0, 0
  for i in range(size-1, -1, -1): # satisfy P(i,j) = True, P(i+1, j-1) = True and
    for j in range(i, size):      # s[i] == s[j], Base case: s[i] = True
      if i == j:
        dp[0][j] = True
      elif j == i + 1:
        dp[0][j] = (s[i] == s[j])
      else:
        dp[0][j] = dp[1][j-1] and s[i] == s[j]
      if dp[0][j] and j-i+1 > max_len:
        max_i, max_j, max_len = i, j, j-i+1
    dp[0], dp[1] = dp[1], dp[0]      # dp[0]: currently results;
  return s[max_i:max_j+1]           # dp[1]: last time results



import unittest

class TestLongestPalinSubstring(unittest.TestCase):
  def test_longest_palindromic_substirng(self):
    self.assertIn(longestPalindrome('babad'), ('bab', 'aba'))
    self.assertEqual(longestPalindrome('abcdzdcab'), 'cdzdc')



if __name__ == '__main__':
  unittest.main()