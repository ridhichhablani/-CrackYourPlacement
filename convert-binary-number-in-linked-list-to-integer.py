# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        temp=head
        res=""
        while temp is not None:
            res+=str(temp.val)
            temp=temp.next
        integer=int(res,2)
        return integer
        
