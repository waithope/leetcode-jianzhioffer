# Description
# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines,
# which together with x-axis forms a container,
# such that the container contains the most water.
# Note: You may not slant the container and n is at least 2.

# y ^
#     |
#     |     a2
#     |     |  a3          an
#     |  a1 |  |     a5    |
#     |  |  |  |  a4 |     |
#     |  |  |  |  |  | ..  |
#     --------------------------->
#    0   1  2  3  4  5 ..  n     x

# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49

def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    maxarea = 0
    l, r = 0, len(height) - 1
    while l < r:
      maxarea = max(maxarea, min(height[l], height[r]) * (r - l))
      if height[l] < height[r]:
        l += 1
      else:
        r -= 1
    return maxarea