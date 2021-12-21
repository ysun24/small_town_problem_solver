from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums)-1
        while i < j:
            if nums[i] == val:
                while j > i and nums[j] == val:
                    j -= 1
                if j == i:
                    break
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
        
        return (i+1) if nums[j] != val else i