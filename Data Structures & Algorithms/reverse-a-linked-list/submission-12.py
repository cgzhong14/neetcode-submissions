# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        
        while(head):
            # Save the next node before we break the link
            temp = head.next
            
            # Reverse the current node's pointer
            head.next = prev
            
            # Move prev forward to current node
            prev = head
            
            # Move head forward to the saved next node
            head = temp
        
        # prev is now pointing to the new head of the reversed list
        return prev


