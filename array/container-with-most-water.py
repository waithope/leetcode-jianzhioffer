

# y ^
#     |
#     |     a2
#     |     |  a3          an
#     |  a1 |  |     a5    |
#     |  |  |  |  a4 |     |
#     |  |  |  |  |  | ..  |
#     --------------------------->
#    0   1  2  3  4  5 ..  n     x


def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    maxarea = 0
    l,r = 0, len(height) - 1
    while l < r:
      maxarea = max(maxarea, min(height[l], height[r]) * (r - l))
      if height[l] < height[r]:
        l += 1
      else:
        r -= 1
    return maxarea