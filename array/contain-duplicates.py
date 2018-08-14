## Description
## Given an array of integers, find if the array contains any duplicates.
## Your function should return true if any value appears at least twice
## in the array, and it should return false if every element is distinct.
## Input: [1,2,3,1]
## Output: true
## Input: [1,2,3,4]
## Output: false

def containsDuplicate(nums):
  """
  :type nums: List[int]
  :rtype: bool
  """
  return len(set(nums)) < len(nums)
  #d = {}
  #for num in nums:
  #    if num in d:
  #        return True
  #    else:
  #        d[num] = num
  #return False


import unittest

class TestContainDuplicates(unittest.TestCase):
  def test_contain_duplicates(self):
    self.assertEqual(containsDuplicate([1]), False)
    self.assertEqual(containsDuplicate([1,2,3,1]), True)
    self.assertEqual(containsDuplicate([1,2,3,4]), False)
    self.assertEqual(containsDuplicate([1,1,1,3,3,4,3,2,4,2]), True)


if __name__ == '__main__':
  unittest.main()

