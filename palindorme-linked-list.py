# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp=head
        ar=[]
        while temp is not None:
            ar.append(temp.val)
            temp=temp.next
            
        if ar==ar[::-1]:
            return True
        return False
        
        
