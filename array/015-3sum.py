## Description
## Given an array nums of n integers, are there elements a, b, c in nums
## such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

##The solution set must not contain duplicate triplets.

## Given array nums = [-1, 0, 1, 2, -1, -4],
## A solution set is:
## [
##   [-1, 0, 1],
##   [-1, -1, 2]
## ]
## Given [0, 0, 0, 0], solution [[0, 0, 0]]
## Given [-1, -1, 0, 1], solution [[-1, 0 , 1]]



## Complexity Time O(n*n)
def threeSum(nums):
	"""
	:type nums: List[int]
	:rtype: List[List[int]]
	"""
	n = len(nums)
	if n < 3:
		return []
	nums.sort()
	res = []
	for i in range(n-2):
		if i > 0 and nums[i] == nums[i-1]:            # skip duplicates
			continue
		j = i + 1
		k = n - 1
		while j < k:
			s = nums[i] + nums[j] + nums[k]
			if s == 0:
				res.append([nums[i], nums[j], nums[k]])
				while j < k and nums[j] == nums[j+1]:     # remove duplicates
					j += 1
				while j < k and nums[k] == nums[k-1]:
					k -= 1
				j += 1
				k -= 1
			elif s < 0:
				j += 1
			else:
				k -= 1
	return res


import unittest

class TestThreeSum(unittest.TestCase):
	def test_three_sum(self):
		self.assertEqual(threeSum([0,0,0,0]), [[0,0,0]])
		self.assertEqual(threeSum([-1,0,-1,1]), [[-1,0,1]])
		self.assertEqual(threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2],[-1, 0, 1]])


if __name__ == '__main__':
	unittest.main()

