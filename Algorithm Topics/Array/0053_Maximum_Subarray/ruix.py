from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i_sum = nums[0]     # i_sum is the max sum of sequences ending in index i.
        max_sum = i_sum     # max_sum is the max of the sequences seen so far.

        for i in range(1, len(nums)):
            if i_sum < 0:           # the sequence ending in i definitely would be nums[i] itself.
                i_sum = nums[i]
            else:              
                i_sum += nums[i]
            
            max_sum = max(max_sum, i_sum)
        
        return max_sum