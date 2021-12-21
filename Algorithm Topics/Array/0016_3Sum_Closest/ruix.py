from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        s_closest = float('inf')

        nums.sort()
        i = 0
        while i < len(nums):            
            j = i + 1
            k = len(nums)-1
            while (j < k):
                _sum = target - nums[i]
                if nums[j] + nums[k] == _sum:
                    return target
                elif (nums[j] + nums[k] < _sum):
                    s_closest = min(s_closest, nums[i] + nums[j] + nums[k], key=lambda x: abs(x-target))
                    j += 1
                else:
                    s_closest = min(s_closest, nums[i] + nums[j] + nums[k], key=lambda x: abs(x-target))
                    k -= 1

            l = i + 1
            while (l < len(nums) and nums[i] == nums[l]):
                l += 1
            i = l
                    
        
        return s_closest

sol = Solution()
print(sol.threeSumClosest([-1,2,1,-4], 1))