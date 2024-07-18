class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        size=len(nums2)
        for _ in range(size):
            i=len(nums1)-1
            nums1.pop()
            i-=1
        for i in nums2:
            nums1.append(i)
        
        return nums1.sort()


    
