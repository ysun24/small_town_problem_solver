from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def search(cand: List[int], stk: List[int], target: int):
            for i in range(len(cand)):
                if cand[i] == target:
                    res.append(stk + [cand[i]])
                elif cand[i] < target:
                    search(cand[i:], stk + [cand[i]], target-cand[i])
        
        search(candidates, [], target)

        return res