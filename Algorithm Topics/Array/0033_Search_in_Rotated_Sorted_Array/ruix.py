from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        pivot = self.find_pivot(nums)
        real_nums = nums[pivot:] + nums[:pivot]

        a = self.binary_search(target, real_nums)
        if a == -1:
            return a
        return (a + pivot) % len(nums)

    
    def find_pivot(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        mid = n // 2 if n%2 else n//2-1
        if nums[mid] > nums[mid+1]:
            return mid+1
        else:
            a = self.find_pivot(nums[:mid+1])
            if a != 0: return a
            a = self.find_pivot(nums[mid+1:])
            if a == 0: return 0
            return a + mid+1
    
    def binary_search(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        if not n or (n == 1 and nums[0] != target):
            return -1
        mid = n // 2 if n%2 else n//2-1
        if nums[mid] == target:
            return mid
        else:
            a = self.binary_search(target, nums[:mid+1])
            if a != -1: return a
            a = self.binary_search(target, nums[mid+1:])
            if a != -1: return a + mid+1
            return -1