from typing import List
import math
from collections import deque


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        nr = len(grid)
        nc = len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        total_sum = [[0] * nc for _ in range(nr)]

        def bfs(r, c, curr_count):
            min_distance = math.inf
            queue = deque([[r, c, 0]])

            while queue:
                curr_r, curr_c, curr_step = queue.popleft()

                for d in dirs:
                    next_r = curr_r + d[0]
                    next_c = curr_c + d[1]

                    if 0 <= next_r < nr and 0 <= next_c < nc and grid[next_r][next_c] == -curr_count:
                        total_sum[next_r][next_c] += curr_step + 1
                        min_distance = min(min_distance, total_sum[next_r][next_c])
                        grid[next_r][next_c] -= 1
                        queue.append([next_r, next_c, curr_step + 1])

            return min_distance

        count = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 1:
                    min_distance = bfs(r, c, count)
                    count += 1
                    print(r, c, grid, min_distance)
                    print(total_sum)

                    if min_distance == math.inf:
                        return -1

        return min_distance


if __name__ == "__main__":
    grid = [[1, 0, 2, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0]]
    solution = Solution()
    print(solution.shortestDistance(grid))
