from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        
        nums.sort()
        
        res = []
        i = 0
        while i < len(nums):
            _res = self.permuteUnique(nums[:i] + nums[i+1:])
            res.extend([[nums[i]] + _r for _r in _res])

            j = i + 1
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            i = j
        
        return res