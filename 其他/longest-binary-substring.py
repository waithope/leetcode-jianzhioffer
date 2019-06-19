
## Description
## Given a string composed of 0 and 1, find a longest substring
## which has same number of 0 and 1
## Given a = '1011010', the longest is '011010', 6
## Given b = '10110100', the longest is itself '10110100', 8

def longestOfBinarySubstring(s):
  count = [0, 0]
  B = [0] * len(s)
  longest = 0
  diff = {}
  for i in range(len(s)):
    count[int(s[i])] += 1
    B[i] = count[0] - count[1]  # the difference of 0 and 1
    if B[i] == 0:
      longest = i + 1       # from the start to i, the number of 0 and 1 are same,
      continue              # since list index start at 0
    if B[i] in diff:
      longest = max(longest, i - diff[B[i]])
    else:
      diff[B[i]] = i
  return longest



import unittest

class TestLongestBinarySubstring(unittest.TestCase):
  def test_longest_binary_substring(self):
    self.assertEqual(longestOfBinarySubstring('0011110'), 4)
    self.assertEqual(longestOfBinarySubstring('1011010'), 6)
    self.assertEqual(longestOfBinarySubstring('1101000'), 6)
    self.assertEqual(longestOfBinarySubstring('10110100'), 8)
    self.assertEqual(longestOfBinarySubstring('01101100001'), 10)


if __name__ == '__main__':
  unittest.main()
