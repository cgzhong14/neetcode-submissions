# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while(curr):
            #curr cur next a temporary variable
            temp = curr.next
            #make current next point to previous
            curr.next = prev
            #make previous node to the current
            prev = curr
            #make current equal to the temporary (current next)
            curr = temp
        return prev