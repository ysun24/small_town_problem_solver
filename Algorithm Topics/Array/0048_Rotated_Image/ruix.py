from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n == 1:
            return
        
        mid = n//2        
        base = 1 if n%2 else 2
        while base <= n:
            idx_start = mid - base//2
            irow = idx_start
            for j in range(base-1):
                icol = idx_start + j
                temp = matrix[irow][icol]

                # (irow, icol)              (icol, n-1-irow)
                # (n-1-icol, irow)          (n-1-irow, n-1-icol)
                
                matrix[irow][icol] = matrix[n-1-icol][irow]
                matrix[icol][n-1-irow], temp = temp, matrix[icol][n-1-irow]
                matrix[n-1-irow][n-1-icol], temp = temp, matrix[n-1-irow][n-1-icol]
                matrix[n-1-icol][irow] = temp

            base += 2
    
    def print_matrix(self, matrix: List[List[int]]) -> None:
        for row in matrix:
            print([f"{n:>3}" for n in row])