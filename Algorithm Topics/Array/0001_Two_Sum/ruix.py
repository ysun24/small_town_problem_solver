from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_idx = {}
        for i in range(len(nums)):
            if target-nums[i] in num_to_idx.keys():
                return [num_to_idx[target-nums[i]], i]
            else:
                num_to_idx[nums[i]] = i
        return []