from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # heur_grid[i][j] records the number of paths from (i,j) to bottom right.
        heur_grid = [[0 for _ in range(n)] for __ in range(m)]

        # if the bottom right is itself an obstable, then I can never approach it.
        heur_grid[m-1][n-1] = (1 if obstacleGrid[m-1][n-1] == 0 else 0)

        # first, handle the right most column of the grid.
        i = m - 2
        while i >= 0:
            if obstacleGrid[i][n-1] != 1:
                heur_grid[i][n-1] = heur_grid[i+1][n-1]
            i -= 1

        # then, handle the bottom row of the grid.
        j = n - 2
        while j >= 0:
            if obstacleGrid[m-1][j] != 1:
                heur_grid[m-1][j] = heur_grid[m-1][j+1]
            j -= 1

        # handle the rest of the grid row by row. (can also column by column)
        i = m - 2
        while i >= 0:
            j = n - 2
            while j >= 0:
                if obstacleGrid[i][j] != 1:         # There is not an obestacle here.
                    left_paths = heur_grid[i][j+1]
                    down_paths = heur_grid[i+1][j]
                    heur_grid[i][j] = left_paths + down_paths
                j -= 1
            i -= 1
        
        return heur_grid[0][0]

    def print_matrix(self, matrix: List[List[int]]) -> None:
        for row in matrix:
            print([f"{n:>3}" for n in row])