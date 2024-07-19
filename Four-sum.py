class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        unique=set()

        
        #result=[]

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                k=j+1
                l=len(nums)-1
                while k<l:
                    
 
                    total=nums[i]+nums[j]+nums[k]+nums[l]
                    if total>target:
                        l-=1
                    elif total<target:
                        k+=1
                    else:
                        temp=[nums[i],nums[j],nums[k],nums[l]]
                        unique.add(tuple(temp))
                        k+=1
                        l-=1
        result=list(unique)
        return result

        
