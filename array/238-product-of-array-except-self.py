# Description
# Given an array nums of n integers where n > 1,
# return an array output such that output[i] is equal to the product
# of all the elements of nums except nums[i].
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Note: Please solve it without division and in O(n).
# solve it with constant space complexity?
# (The output array does not count as extra space for
# the purpose of space complexity analysis.)


def productExceptSelf(nums):
  """
  :type nums: List[int]
  :rtype: List[int]
  """
  #mul = 1
  #aux = [0 for i in range(len(nums))]
  #for i in range(len(nums))[::-1]:
  #    res = nums[i] * mul
  #    aux[i] = res
  #    mul = res
  #aux.append(1)
  #
  #pre = 1
  #output = [0 for i in range(len(nums))]
  #for i in range(len(nums)):
  #    output[i] = pre*aux[i+1]
  #    pre = pre * nums[i]
  #return output

  if not nums:
    return

  pre, output = 1, []
  for i in range(len(nums)):
    output.append(pre)
    pre = pre * nums[i]

  pre = 1
  for i in range(len(nums)-1, -1, -1):
    output[i] = pre * output[i]
    pre = pre*nums[i]
  return output


import unittest

class Test_Product_of_Array_Except_Self(unittest.TestCase):
  def test_product_of_array_except_self(self):
    self.assertEqual(productExceptSelf([1,2,3,4]), [24,12,8,6])
    self.assertEqual(productExceptSelf([2,3,4,5,6]), [360,240,180,144,120])


if __name__ == '__main__':
  unittest.main()