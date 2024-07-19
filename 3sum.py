class Solution:
    def threeSum(self, num: List[int]) -> List[List[int]]:
        unique=set()
        result=[]
        num.sort()
        for i in range(len(num)):
            left=i+1
            right=len(num)-1
            
            while left<right:
                total=num[i]+num[left]+num[right]
                
                if total>0:
                    right-=1
                elif total<0:
                    left+=1
                else:
                    unique.add((num[i],num[left],num[right]))
                    left+=1
        for i in unique:
            result.append(list(i))
        return result

 
