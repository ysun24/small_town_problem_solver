from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        i = 0
        nums.sort()
        while i < len(nums) - 3:
            _nums = nums[i+1:]
            _res = self.threeSum(_nums, target - nums[i])
            for _r in _res:
                res.append([nums[i]] + _r)
            
            l = i + 1
            while (l < len(nums) and nums[l] == nums[i]):
                l += 1
            i = l
        
        return res
    
    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        i = 0
        while i < len(nums):
            _sum = target - nums[i]
            
            j = i + 1
            k = len(nums)-1
            while (j < k):
                if nums[j] + nums[k] == _sum:
                    res.append([nums[i], nums[j], nums[k]])
                    while (j < k and nums[j+1] == nums[j]):
                        j += 1
                    while (k > j and nums[k-1] == nums[k]):
                        k -= 1
                    j, k = j+1, k-1
                elif (nums[j] + nums[k] < _sum):
                    j += 1
                else:
                    k -= 1

            l = i + 1
            while (l < len(nums) and nums[i] == nums[l]):
                l += 1
            i = l
                    
        
        return res