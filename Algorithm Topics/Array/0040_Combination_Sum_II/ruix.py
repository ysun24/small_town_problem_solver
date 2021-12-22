from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if target == 0:
            return [[]]
        
        candidates.sort()

        res = []
        i = 0
        while i < len(candidates):
            if candidates[i] > target: break
            _res = self.combinationSum2(candidates[i+1:], target - candidates[i])
            res.extend([[candidates[i]] + _r for _r in _res])

            j = i + 1
            while (j < len(candidates) and candidates[j] == candidates[i]):
                j += 1
            i = j
        
        return res