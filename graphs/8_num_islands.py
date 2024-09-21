from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    num_islands += 1

        return num_islands

    def dfs(self, grid, row, col):
        if (row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != "1"):
            return

        grid[row][col] = "0"
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row + 1, col)
        self.dfs(grid, row, col - 1)
        self.dfs(grid, row, col + 1)


if __name__ == '__main__':
    solution = Solution()
    grid = [
        ['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0']
    ]
    print(solution.numIslands(grid))

    grid = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
    ]
    print(solution.numIslands(grid))

    grid = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '1', '0'],
        ['0', '0', '0', '0', '0']
    ]
    print(solution.numIslands(grid))
