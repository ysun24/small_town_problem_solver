from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        sprial_mat = []
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return sprial_mat

        sprial_mat.extend(matrix[0])
        if len(matrix) == 1:
            return sprial_mat
        
        for i in range(1, len(matrix)-1):
            sprial_mat.append(matrix[i][-1])
        
        sprial_mat.extend(reversed(matrix[-1]))

        if len(matrix) == 2 or len(matrix[0]) == 1 :
            return sprial_mat

        i = len(matrix) - 2
        while i > 0:
            sprial_mat.append(matrix[i][0])
            i -= 1

        sprial_mat.extend(self.spiralOrder([row[1:-1] for row in matrix[1:-1]]))
        
        return sprial_mat

    def print_matrix(self, matrix: List[List[int]]) -> None:
        for row in matrix:
            print([f"{n:>3}" for n in row])