from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1     # First and last heights.
        min_height = min(height[i], height[j])  # Record the currently lowest height to accelerate.
        max_area = min_height * (j-i)   # Minimum height threshold.

        while (j > i):
            # Eliminate the smaller height.
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

            cur_height = min(height[i], height[j])  # Record the height of the current container.
            if min_height >= cur_height:
                # The width corresponding to min height must be larger than current width,
                # so this height cannot produce larger volume than min-height.
                continue
                
            cur_area = cur_height * (j-i)
            if max_area < cur_area:
                min_height = cur_height
                max_area = cur_area
                
        return max_area

'''
Statement: if height[i] < height[j], then any container taking height[j'] with j' < j would have smaller
area.

Proof:
i < len(nums)-1, j = whatever index > i, height[i] < height[j]. Area of (i,j) is height[i] * (j-i). 
Then any container (i, j') with j' < j would have area = min(height[i], height[j]) * (j'-i). It is 
apparently seen that min(height[i], height[j]) <= height[i] and as j' < j, we can see that base case is 
true.

Similar proof for any j.
'''