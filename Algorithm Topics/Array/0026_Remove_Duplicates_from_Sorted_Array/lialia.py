class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        disc={}
        index=0
        for i in nums:
            if (target-i) not in disc.keys():
                disc[i]=index
            else:
                return [disc[target-i],index]
            index+=1