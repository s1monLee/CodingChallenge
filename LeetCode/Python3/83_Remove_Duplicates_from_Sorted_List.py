# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        h = head
        while h != None and h.next != None:
            if h.val == h.next.val:
                h.next = h.next.next
            else:
                h = h.next
        return head
