'''
    Largest Rectangle in Histogram
=======================================
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
Example:

Input: [2,1,5,6,2,3]
Output: 10
'''

def largestRectangleArea(heights) -> int:
    '''
    思路：以第i个bar为中心，计算这个bar的左边有多少个bar是大于等于它，然后计算
    这个bar的右边有多少个bar是大于等于它的，将结果记录在两个数组left, right，
    分别表示左边和右边。因此，以该bar为中心的最大矩形就是heights[i] * (left[i]
    + right[i] - 1)，最后遍历完n个bar之后，取最大的作为输出。
    '''
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