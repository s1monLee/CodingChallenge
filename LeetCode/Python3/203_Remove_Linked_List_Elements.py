# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        while head and head.val == val:
            head = head.next
        if not head:
            return None
        h = head
        while h.next:
            if h.next.val == val:
                h.next = h.next.next
                continue
            h = h.next
        return head
