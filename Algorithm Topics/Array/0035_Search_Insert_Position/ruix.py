from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        _n = len(nums)
        if _n == 0: return 0
        if _n == 1: return (0 if nums[0] >= target else 1)

        mid = _n//2 if _n%2 else _n//2 - 1
        if nums[mid] == target: return mid
        if mid != 0:
            if nums[mid-1] < target and nums[mid] > target:
                return mid
        if nums[mid] < target and nums[mid+1] > target:
            return mid+1
        
        if target < nums[mid]:
            return self.searchInsert(nums[:mid], target)
        return self.searchInsert(nums[mid+1:], target) + mid+1

sol = Solution()
print(sol.searchInsert([1,3,5,6], 7))