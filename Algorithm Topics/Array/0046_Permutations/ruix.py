from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        
        res = []
        for i in range(len(nums)):
            _res = self.permute(nums[:i] + nums[i+1:])
            res.extend([[nums[i]] + _r for _r in _res])
        
        return res

sol = Solution()
print(sol.permute([1,2,3]))