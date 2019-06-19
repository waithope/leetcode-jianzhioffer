'''
           Happy Number
===================================
Write an algorithm to determine if a number is "happy".
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number
by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''

def isHappy(n):
  """
  :type n: int
  :rtype: bool
  """
#    def calc(number, seen):
#        if number == 1:
#            return True
#
#        res = 0
#        for part in str(number):
#            res += int(part) ** 2
#        if res in seen:
#            return False
#        else:
#            seen.append(res)
#        return calc(res, seen)
#
#    seen = []
#    return calc(n, seen)

  seen = []
  while n not in seen:
    seen.append(n)
    n = sum([int(part)**2 for part in str(n)])
  return n == 1


import unittest

class Test_Happy_Number(unittest.TestCase):
  def test_happy_number(self):
    self.assertEqual(isHappy(2), False)
    self.assertEqual(isHappy(19), True)

if __name__ == '__main__':
  unittest.main()