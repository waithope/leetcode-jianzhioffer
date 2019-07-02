'''
    Maximal Rectangle
=========================
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
'''

def maximalRectangle(matrix) -> int:
    '''
    思路：这道题可以转化成 084-largest rectangle in histogram的形式来做
    '''
    def largestRectangleArea(heights):
        if not isinstance(heights, list) or len(heights) == 0:
            return 0
        n = len(heights)
        left, right = [1] * n, [1] * n
        # compute left
        for i in range(n):
            j = i - 1
            while j >= 0:
                if heights[j] >= heights[i]:
                    left[i] += left[j]
                    j -= left[j]
                else: break

        # compute right
        for i in range(n - 1, -1, -1):
            j = i + 1
            while j < n:
                if heights[j] >= heights[i]:
                    right[i] += right[j]
                    j += right[j]
                else:
                    break

        maxRect = 0
        for i in range(n):
            maxRect = max(maxRect, heights[i] * (left[i] + right[i] - 1))
        return maxRect

    if (not isinstance(matrix, list)
        or not matrix or not matrix[0]):
        return 0

    m, n = len(matrix), len(matrix[0])
    heights = [0] * n
    maxArea = -1
    for row in matrix:
        for i in range(n):
            if row[i] == '1':
                heights[i] += 1
            else:
                heights[i] = 0
        maxRect = largestRectangleArea(heights)
        maxArea = max(maxArea, maxRect)
    return maxArea