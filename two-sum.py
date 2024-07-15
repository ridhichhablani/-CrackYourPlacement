class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[]
        for i in range(1,len(nums)):
            #for j in range(1,len(nums)):
                if nums[i-1]+nums[i]==target:
                        res.append(index(i-1))
                        res.append(index(i))

                        
        return res

        
