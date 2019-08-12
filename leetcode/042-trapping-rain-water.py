#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
class Solution:
    def trap(self, height: List[int]) -> int:
        if not isinstance(height, list) or len(height) <= 1:
            return 0

        leftMax, rightMax = -1, -1
        left, right = 0, len(height) - 1
        res = 0
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])

            # 对每一个位置都计算能够储存的水量，根据木桶原理，如果
            # 当前左边最长的bar小于右边最长的bar，表明被圈住的区域
            # 能够存储到水量
            if leftMax < rightMax:
                res += leftMax - height[left]
                left += 1
            else:
                res += rightMax - height[right]
                right -= 1
        return res

