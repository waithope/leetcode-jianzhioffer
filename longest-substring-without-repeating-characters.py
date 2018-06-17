
## Description
## Given a string, find the length of the longest substring without repeating characters.
## Given "abcabcbb", the answer is "abc", which the length is 3.
## Given "bbbbb", the answer is "b", with the length of 1.


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    start = maxlen = 0
    used = { }
    for i in range(len(s)):
        if s[i] in used and start <= used[s[i]]:
            start = used[s[i]] + 1
        else:
            maxlen = max(maxlen, i - start + 1)

        used[s[i]] = i
    return maxlen


import unittest

class TestLongestString(unittest.TestCase):
  def test_longest_string(self):
    self.assertEqual(lengthOfLongestSubstring('abcabcbb'), 3)
    self.assertEqual(lengthOfLongestSubstring('bbbbb'), 1)
    self.assertEqual(lengthOfLongestSubstring('pwwkew'), 3)

if __name__ == '__main__':
  unittest.main()