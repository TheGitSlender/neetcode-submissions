# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast_head = head
        slow_head = head
        while fast_head != None:
            try:
                fast_head = fast_head.next.next
            except AttributeError:
                return False
            slow_head = slow_head.next
            if fast_head == slow_head:
                return True
        return False