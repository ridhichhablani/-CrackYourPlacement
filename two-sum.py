class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #a=set()
        for i in range(len(nums)-1):
            for j in range(1,len(nums)):
                if (i!=j and nums[i]+nums[j]==target):
                   return [i,j]



  

        
