'''
          Group Anagrams
===================================
Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
All inputs will be in lowercase.
The order of your output does not matter.
'''

def groupAnagrams(strs):
  """
  :type strs: List[str]
  :rtype: List[List[str]]
  """
  seen = {}
  for str in strs:
    seen[tuple(sorted(str))] = seen.get(tuple(sorted(str)), []) + [str]

  return [seen[key] for key in seen.keys()]


import unittest

class Test_Group_Anagrams(unittest.TestCase):
  def test_group_anagrams(self):
    self.assertEqual(groupAnagrams(['eat','tea','tan','ate','nat','bat']),
                                   [['eat','tea','ate'],['tan','nat'],['bat']])
    self.assertEqual(groupAnagrams(['eat','tea','boo','ate','bob','bob']),
                                   [['eat','tea','ate'],['boo'],['bob','bob']])


if __name__ == '__main__':
  unittest.main()