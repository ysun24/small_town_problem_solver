from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        num_to_pos = {}
        for irow in range(len(board)):
            for icol in range(len(board[0])):
                i = board[irow][icol]
                if i == '.':
                    continue
                if i not in num_to_pos.keys():
                    num_to_pos[i] = [[irow], [icol]]
                else:
                    if irow in num_to_pos[i][0] or icol in num_to_pos[i][1]:
                        return False
                    num_to_pos[i][0].append(irow)
                    num_to_pos[i][1].append(icol)
        
        for _i in range(10):
            i = str(_i)
            if i not in num_to_pos.keys():
                continue

            for idx in range(len(num_to_pos[i][0])):
                for jdx in range(len(num_to_pos[i][0])):
                    if jdx == idx: continue

                    nrow = num_to_pos[i][0][idx]
                    mrow = num_to_pos[i][0][jdx]

                    ncol = num_to_pos[i][1][idx]
                    mcol = num_to_pos[i][1][jdx]

                    if nrow // 3 == mrow // 3 \
                        and ncol // 3 == mcol // 3:
                        return False
        return True

board = \
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

sol = Solution()
print(sol.isValidSudoku(board))