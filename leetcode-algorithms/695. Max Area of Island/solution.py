# Given a non-empty 2D array grid of 0's and 1's,
# an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)' \
#                          ' You may assume all four edges of the grid are surrounded by water.
# Find the maximum area of an island in the given 2D array.
# (If there is no island, the maximum area is 0.)


class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])

        def dfs(i, j):
            if 0 <= i < row and 0 <= j < col and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i-1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1)
            return 0

        max_area = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    max_area = max(dfs(i, j), max_area)
        return max_area
