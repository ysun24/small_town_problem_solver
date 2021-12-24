from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)    
        ttl_len = len1+len2
        # The min length at which nums(below) contains necessary elements to calculate median.
        mid_len = ttl_len // 2 + 1   
        
        nums = []   # Merge nums1 and nums2 in ascending order into nums.
        i, j = 0, 0
        while (i < len1 and j < len2):
            if (nums1[i] < nums2[j]):
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
                
            if len(nums) == mid_len:
                # If nums already achieves mid length, return.
                return self.whatToReturn(nums, ttl_len%2)
        
        # In case nums1 is longer.
        while (i < len1):
            nums.append(nums1[i])
            i += 1
            if len(nums) == mid_len:
                return self.whatToReturn(nums, ttl_len%2)
        # In case nums2 is longer.
        while (j < len2):
            nums.append(nums2[j])
            j += 1
            if len(nums) == mid_len:
                return self.whatToReturn(nums, ttl_len%2)
        
    def whatToReturn(self, nums, odd):
        if odd:
            return nums[-1]
        else:
            return (nums[-2] + nums[-1]) / 2

'''
Merge nums1 and nums2 into a single array "nums" in ascending order until middle length is achieved.
Then if total length is odd, return last element of nums, otherwise return avergae of the last two 
elements of nums.
'''