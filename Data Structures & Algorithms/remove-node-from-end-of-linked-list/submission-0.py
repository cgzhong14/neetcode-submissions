# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        findCur = head
        array = []
        while findCur:
            array.append(findCur)
            findCur = findCur.next
        removeNode = array[len(array)-n]
        
        prev = dummy
        replace = head
        while replace:
            if replace == removeNode:
                prev.next = replace.next
                break
            prev = replace
            replace = replace.next
        return dummy.next
