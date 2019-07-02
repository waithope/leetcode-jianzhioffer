## Description
# Given an array of non-negative integers,
# you are initially positioned at the first index of the array.
## Each element in the array represents your *maximum* jump length at that position.
## Determine if you are able to reach the last index.
## Input: [2,3,1,1,4]
## Output: true
## Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
## Input: [3,2,1,0,4]
## Output: false
## Explanation: You will always arrive at index 3 no matter what.
## Its maximum jump length is 0, which makes it impossible to reach the last index.

def canJump(nums):
  """
  :type nums: List[int]
  :rtype: bool
  """
  ## backtracking
  #def canJumpFromPosition(pos, nums):
  #    if pos == len(nums)-1:
  #        return True
  #
  #    furthestJump = min(pos+nums[pos], len(nums)-1)
  #    pos += 1
  #    while pos <= furthestJump:
  #        if canJumpFromPosition(pos, nums):
  #            return True
  #    return False
  #
  #return canJumpFromPosition(0, nums)

  ## dynamic programming top-down
  ## 'G' for Good position, 'B' for Bad position, 'U' for Unknown
  #def canJumpFromPosition(pos, nums):
  #    #if memo[pos] == 'G':
  #    #    return True
  #    #elif memo[pos] == 'B':
  #    #    return False
  #    if memo[pos] != 'U':
  #        return memo[pos] == 'G'
  #
  #
  #    furthestJump = min(pos+nums[pos], len(nums)-1)
  #    for i in range(pos+1, furthestJump+1):
  #        if canJumpFromPosition(i, nums):
  #            memo[pos] = 'G'
  #            return True
  #    memo[pos] = 'B'
  #    return False
  #
  #memo = ['U' for i in range(len(nums))]
  #memo[-1] = 'G'
  #return canJumpFromPosition(0, nums)

  ## dynamic programming bottom-up
  #memo = ['U' for i in range(len(nums))]
  #memo[-1] = 'G'
  #
  #for i in range(len(nums)-1)[::-1]:
  #    furthestJump = min(i+nums[i], len(nums)-1)
  #    for j in range(i+1, furthestJump+1):
  #        if memo[j] == 'G':
  #            memo[i] = 'G'
  #            break
  #return memo[0] == 'G'

  ## greedy
  #reachable = 0
  #for i, num in enumerate(nums):
  #    if i > reachable:
  #        return False
  #    else:
  #        reachable = max(reachable, i+num)
  #return True

  lastpos = len(nums) - 1
  for i in range(len(nums)-1)[::-1]:
      reach = i + nums[i]
      if reach >= lastpos:
          lastpos = i
  return lastpos == 0


import unittest

class Test_Jump_Game(unittest.TestCase):
  def test_jump_game(self):
    self.assertEqual(canJump([2,0,0]), True)
    self.assertEqual(canJump([2,3,1,1,4]), True)
    self.assertEqual(canJump([3,2,1,0,4]), False)


if __name__ == '__main__':
  unittest.main()