#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):
            if (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0])
                or grid[i][j] != '1'):
                return
            grid[i][j] = '#'
            dfs(grid, i - 1, j)
            dfs(grid, i + 1, j)
            dfs(grid, i, j - 1)
            dfs(grid, i, j + 1)

        if (not isinstance(grid, list) or len(grid) == 0
            or not isinstance(grid[0], list) or len(grid[0]) == 0):
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
        return count



