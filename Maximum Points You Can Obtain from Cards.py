class Solution:
    def maxScore(self, num: List[int], k: int) -> int:
        left=k-1
        right=len(num)-1
        pick=sum(num[:k])
        maxi=pick
        for _ in range(k):
            pick+=(num[right]-num[left])
            maxi=max(maxi,pick)
            left-=1
            right-=1
        return maxi




        
