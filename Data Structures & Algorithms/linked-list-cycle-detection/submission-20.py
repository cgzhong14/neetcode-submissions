# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while(slow and fast):
            if slow.val == fast.val:
                return True
            if fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            else:
                return False
        return False