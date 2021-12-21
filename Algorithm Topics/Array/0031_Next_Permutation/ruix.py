from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = len(nums) - 1
        i = -1
        
        while j > 0:
            i = j - 1
            if i >= 0 and nums[i] < nums[j]:
                break               
            j -= 1
        
        if j == 0:
            self.bubbleSort(0, nums)
        else:
            k = len(nums)-1
            while k > i and nums[k] <= nums[i]:
                k -= 1
            nums[k], nums[i] = nums[i], nums[k]
            self.bubbleSort(j, nums)
    
    def bubbleSort(self, idx: int, nums: List[int]) -> None:
        for i in range(idx, len(nums)-1):
            for j in range(idx, len(nums)-1-(i-idx)):
                if (nums[j] >= nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]

'''
Proof by contradiction:
Suppose there is another optimal permutation that is smaller than the one written above. In the optimal
permutation, the very first number different from the original version is j, and the number in this
position in the original version is i. j must be > i, otherwise the number shrinks. j must had been beh-
ind i. However, if i was not the peak number, then this permutation must be larger than the permutation
that was given in my function.
'''