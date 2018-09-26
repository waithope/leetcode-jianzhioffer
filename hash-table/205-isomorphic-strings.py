'''
        Isomorphic Strings
===================================
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character
while preserving the order of characters.
No two characters may map to the same character but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
'''

def isIsomorphic(s, t):
  """
  :type s: str
  :type t: str
  :rtype: bool
  """
  #ds, dt = {}, {}
  #for i, ch in enumerate(s):
  #    if ch in ds:
  #        ds[ch].append(i)
  #    else:
  #        ds[ch] = [i]
  #for i, ch in enumerate(t):
  #    if ch in dt:
  #        dt[ch].append(i)
  #    else:
  #        dt[ch] = [i]
  #
  #for i in range(len(s)):
  #    if ds[s[i]] != dt[t[i]]:
  #        return False
  #return True

  #ds, dt = {}, {}
  #for i, ch in enumerate(s):
  #    ds[ch] = ds.get(ch, []) + [i]
  #for i, ch in enumerate(t):
  #    dt[ch] = dt.get(ch, []) + [i]
  #return sorted(ds.values()) == sorted(dt.values())

  def trans(string):
    res, cur = '', 'a'
    mapping = {}
    for ch in string:
      if ch in mapping:
        res += mapping[ch]
      else:
        mapping[ch] = cur
        res += cur
        cur = chr(ord(cur)+1)
    return res

  return trans(s) == trans(t)


import unittest

class Test_Isomorphic_Strings(unittest.TestCase):
  def test_isomorphic_strings(self):
    self.assertEqual(isIsomorphic('egg', 'add'), True)
    self.assertEqual(isIsomorphic('paper', 'title'), True)
    self.assertEqual(isIsomorphic('foo', 'bar'), False)
    self.assertEqual(isIsomorphic('smell', 'tell'), False)


if __name__ == '__main__':
  unittest.main()
