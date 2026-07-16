# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode()
        temp_list = new_list
        while list1 and list2:
            if list1.val <= list2.val:
                temp_list.next = list1
                list1 = list1.next
            else:
                temp_list.next = list2
                list2 = list2.next
            temp_list = temp_list.next
        if list1 == None:
            temp_list.next = list2
        if list2 == None:
            temp_list.next = list1
        return new_list.next