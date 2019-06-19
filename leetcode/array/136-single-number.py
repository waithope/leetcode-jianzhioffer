# Description
# Given a non-empty array of integers,
# every element appears twice except for one. Find that single one.
# Note:
# Your algorithm should have a linear runtime complexity.
# Could you implement it without using extra memory?
# Input: [2,2,1]
# Output: 1
# Input: [4,1,2,1,2]
# Output: 4

def singleNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #cache = {}
        #for num in nums:
        #    if num in cache:
        #        cache[num] += 1
        #    else:
        #        cache[num] = 1
        #
        #for num in set(nums):
        #    if cache[num] == 1:
        #        return num
        #return

        #return reduce(lambda x, y: x ^ y, nums)
        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]
        return res


import unittest

class Test_Single_Number(unittest.TestCase):
  def test_single_number(self):
    self.assertEqual(singleNumber([0]), 0)
    self.assertEqual(singleNumber([2,2,1]), 1)
    self.assertEqual(singleNumber([4,1,2,1,2]), 4)

if __name__ == '__main__':
  unittest.main()