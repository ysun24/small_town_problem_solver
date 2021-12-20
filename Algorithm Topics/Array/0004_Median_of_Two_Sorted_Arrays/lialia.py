class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        index1=0
        index2=0
        l=(len(nums1)+len(nums2)) / 2
        flag=(len(nums1)+len(nums2)) % 2
        
        if(len(nums1)>index1):
            num1=nums1[index1]
        else:
            num1=float('inf')
            
        if(len(nums2)>index2):
            num2=nums2[index2]
        else:
            num2=float('inf')
        
        tempList=[]
        while len(tempList)<=l:
            if num1<num2:
                tempList.append(num1)
                index1+=1
                if(len(nums1)>index1):
                    num1=nums1[index1]
                else:
                    num1=float('inf')
            else:
                tempList.append(num2)
                index2+=1
                if(len(nums2)>index2):
                    num2=nums2[index2]
                else:
                    num2=float('inf')
                    
        if flag==1:
            return tempList[-1]
        else:
            return (tempList[-1]+tempList[-2])/2.0