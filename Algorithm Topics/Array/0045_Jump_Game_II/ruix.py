from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        _n = len(nums)

        # Base conditions.
        if _n <= 1:
            return 0
        if nums[0] >= _n-1:
            return 1

        # Checked position is the position before which the current position is the best position to
        # stand on.
        current_pos, checked_pos = 0, -1 
        jump_to = current_pos + nums[current_pos]   # the max index I can jump to from current pos.
        n_steps = 0 # number of steps I've taken.

        while jump_to < _n-1:
            current_pos = self.findNextPos(current_pos, checked_pos, nums)
            checked_pos = jump_to
            jump_to = current_pos + nums[current_pos]
            n_steps += 1
        
        return n_steps+1

    def findNextPos(self, current_pos: int, checked_pos: int, nums: List[int]) -> int:
        # By the iteration conditions of the above function, each time this function
        # is called, checked_pos < len(nums)-1.
        new_pos = checked_pos+1
        i = checked_pos+1

        while i <= current_pos + nums[current_pos]:
            if i+nums[i] > new_pos+nums[new_pos]:
                new_pos = i
            i += 1
        
        return new_pos

'''
Easily proved by contradiction that the above function gives optimal solution.
'''