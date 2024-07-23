# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Calculate the length of the linked list
        temp1 = head
        length = 0
        while temp1 is not None:
            temp1 = temp1.next
            length += 1
        
        # Step 2: Find the middle index
        mid = length // 2
        
        # Step 3: Traverse to the middle index
        temp2 = head
        for _ in range(mid):
            temp2 = temp2.next
        
        return temp2

