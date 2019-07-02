## Description
## Given a non-empty array of digits representing a non-negative integer,
## plus one to the integer. The digits are stored such that the
## most significant digit is at the head of the list, and each element
## in the array contain a single digit.
## You may assume the integer does not contain any leading zero,
## except the number 0 itself.
## Input: [1,2,3]
## Output: [1,2,4]
## Explanation: The array represents the integer 123.
## Input: [4,3,2,1]
## Output: [4,3,2,2]
## Explanation: The array represents the integer 4321.


def plusOne(digits):
  """
  :type digits: List[int]
  :rtype: List[int]
  """
  carry = 0
  n = len(digits)
  for i in range(n-1, -1, -1):
    if i == n-1:
      digits[i] += 1
    newdigit = carry + digits[i]
    carry = newdigit // 10
    digits[i] = newdigit % 10

  if carry != 0:
    digits.insert(0, carry)
  return digits



import unittest

class TestPlusOne(unittest.TestCase):
  def test_plus_one(self):
    self.assertEqual(plusOne([9]), [1,0])
    self.assertEqual(plusOne([1,2,3]), [1,2,4])
    self.assertEqual(plusOne([4,3,2,1]), [4,3,2,2])
    self.assertEqual(plusOne([9,9,9,9,9]), [1,0,0,0,0,0])
    self.assertEqual(plusOne([9,6,9,9,9]), [9,7,0,0,0])


if __name__ == '__main__':
  unittest.main()