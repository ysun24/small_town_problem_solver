from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def binary_search_insert(intervals: List[List[int]], newInterval: List[int]) -> int:
            if len(intervals) == 0:
                return 0
            if len(intervals) == 1:
                a = intervals[0]
                b = newInterval
                return 0 if a[0] >= b[0] else 1
            
            n = len(intervals)
            mid = n//2 if n%2 else n//2 - 1
            
            a = intervals[mid]
            b = newInterval

            if a[0] == b[0]: return mid
            if a[0] > b[0]:
                return binary_search_insert(intervals[:mid], b)
            else:
                return binary_search_insert(intervals[mid+1:], b) + mid+1
        
        idx = binary_search_insert(intervals, newInterval)

        intervals = intervals[:idx] + [newInterval] + intervals[idx:]

        i = idx
        if i: i -= 1
        while (i < len(intervals)-1):
            a = intervals[i]
            b = intervals[i+1]

            if a[1] >= b[1]:
                intervals.remove(b)
            elif a[1] >= b[0] and a[1] <= b[1]:
                a[1] = b[1]
                intervals.remove(b)
            else: 
                if i >= idx: break
                i += 1
        
        return intervals

sol = Solution()
print(sol.insert([[0,5],[9,12]], [7,16]))