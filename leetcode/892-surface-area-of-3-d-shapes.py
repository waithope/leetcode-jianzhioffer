#
# @lc app=leetcode id=892 lang=python3
#
# [892] Surface Area of 3D Shapes
#
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        # For each tower, its surface area is 4 * v + 2
        # However, 2 adjacent tower will hide the area of connected part.
        # The hidden part is min(v1, v2) and we need just minus this area * 2
        if not isinstance(grid, list) or len(grid) == 0:
            return 0

        n = len(grid)
        res = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    res += grid[i][j] * 4 + 2
                if i != 0:
                    res -= min(grid[i][j], grid[i-1][j]) * 2
                if j != 0:
                    res -= min(grid[i][j], grid[i][j-1]) * 2
        return res

