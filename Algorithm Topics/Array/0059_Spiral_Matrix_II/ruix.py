from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        def fillMatrix(n: int, idx: int, i_lb: int, mat: List[List[int]]) -> None:
            mid = n//2 if n%2 else n//2 - 1
            if idx > mid:
                return

            irow = idx
            icol = idx
            num = i_lb

            while icol <= n-1-idx:
                mat[irow][icol] = num
                num += 1
                icol += 1
            
            icol -= 1
            irow += 1
            
            while irow <= n-1-idx:
                mat[irow][icol] = num
                num += 1
                irow += 1

            irow -= 1
            icol -= 1

            while icol >= idx:
                mat[irow][icol] = num
                num += 1
                icol -= 1
            
            icol += 1
            irow -= 1

            while irow > idx:
                mat[irow][icol] = num
                num += 1
                irow -= 1
            
            fillMatrix(n, idx+1, num, mat)
        
        matrix = [[0 for _ in range(n)] for __ in range(n)]
        fillMatrix(n, 0, 1, matrix)

        return matrix

    def print_matrix(self, matrix: List[List[int]]) -> None:
        for row in matrix:
            print([f"{n:>3}" for n in row])