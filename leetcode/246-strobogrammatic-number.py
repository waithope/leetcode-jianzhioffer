'''
      Strobogrammatic Number
===================================
A strobogrammatic number is a number that looks the same
when rotated 180 degrees (looked at upside down).
Write a function to determine if a number is strobogrammatic.
The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.
'''

def isStrobogrammatic(num):
  table = {'0':'0', '1':'1', '6':'9', '8':'8','9':'6'}
  n = len(num)
  for i in range(n // 2):
    if num[i] not in table or table[num[i]] != num[n-i-1]:
      return False
  return True

import unittest

class Test_Strobogrammatic_Number(unittest.TestCase):
  def test_strobogrammatic_number(self):
    self.assertEqual(isStrobogrammatic('69'), True)
    self.assertEqual(isStrobogrammatic('88'), True)
    self.assertEqual(isStrobogrammatic('818'), True)
    self.assertEqual(isStrobogrammatic('8138'), False)


if __name__ == '__main__':
  unittest.main()