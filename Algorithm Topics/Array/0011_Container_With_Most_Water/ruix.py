from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        min_height = min(height[i], height[j])
        max_area = min_height * (j-i)
        while (j > i):
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            cur_height = min(height[i], height[j])
            if min_height >= cur_height:
                continue
                
            cur_area = cur_height * (j-i)
            if max_area < cur_area:
                min_height = cur_height
                max_area = cur_area
                
        return max_area