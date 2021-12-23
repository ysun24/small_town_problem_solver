from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        max_pos = 0
        for i in range(len(nums)):
            max_pos = max(nums[i], max_pos-1)

            if max_pos == 0 and i != len(nums)-1:
                return False
        
        return True