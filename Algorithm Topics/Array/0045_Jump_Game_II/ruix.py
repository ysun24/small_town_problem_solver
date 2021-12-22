from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        idx_to_steps = [float('inf')] * len(nums)
        idx_to_steps[len(nums)-1] = [0]

        i = len(nums) - 2
        while i >= 0:
            if nums[i] >= len(nums)-i-1:
                idx_to_steps[i] = 1
            else:
                for n_steps in range(1, nums[i]+1):
                    idx_to_steps[i] = min(idx_to_steps[i+n_steps]+1, idx_to_steps[i])
            i -= 1
        
        return idx_to_steps[0]