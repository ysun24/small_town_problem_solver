from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        _n = len(nums)
        if _n == 0:
            return [-1, -1]
        if _n == 1:
            if nums[0] == target: return [0, 0]
            else: return [-1, -1]
        
        mid = _n // 2 if _n%2 else _n // 2 - 1

        a = self.searchRange(nums[:mid+1], target)
        if a[0] == -1 and a[1] == -1:
            a = self.searchRange(nums[mid+1:], target)
            if a [0] != -1 and a[1] != -1:
                return [a[0] + mid+1, a[1] + mid+1]
            else: return a
        else:
            if nums[mid+1] != target: return a
            else:
                b = self.searchRange(nums[mid+1:], target)
                if b[0] == -1 and b[1] == -1:
                    return a
                else:
                    return [a[0], b[1] + mid+1]

sol = Solution()
print(sol.searchRange([], 0))