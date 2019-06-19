
## Descirption
## Given an array of distinct integers and a sum value.
## Find count of triplets with sum smaller than given sum value.
## Expected Time Complexity is O(n2).
# Input : arr[] = {-2, 0, 1, 3}
#         sum = 2.
# Output : 2
# Explanation :  Below are triplets with sum less than 2
#                (-2, 0, 1) and (-2, 0, 3)

## Brute Force
def countTriplets_BF(nums, sum):
  size = len(nums)
  cnt = 0
  for i in range(size-2):
    for j in range(i+1, size-1):
      for k in range(j+1, size):
        if (nums[i]+nums[j]+nums[k]) < sum:
          cnt += 1
  return cnt

def countTriplets(nums, sum):
  size = len(nums)
  if size < 3 or nums is None:
    return 0

  nums.sort()
  cnt = 0
  for i in range(size-2):
    j = i+1
    k = size-1
    while j < k:
      if (nums[i]+nums[j]+nums[k]) < sum:
        cnt += k - j        # If nums[i] + nums[j] + nums[k] < target, which means
        j += 1              # the numbers between j and k are all less than target(array sorted)
      else:
        k -= 1
  return cnt


import unittest

class TestCountTriplets(unittest.TestCase):
  def test_count_triplets(self):
    self.assertEqual(countTriplets([-2,0,1,3], 2), 2)
    self.assertEqual(countTriplets([5,1,3,4,7], 12), 4)
    self.assertEqual(countTriplets([1,2,3,4,5,6,7,8], 10), 7)
    self.assertEqual(countTriplets([3,7,9,1,2,5,11,4], 10), 6)


if __name__ == '__main__':
  unittest.main()