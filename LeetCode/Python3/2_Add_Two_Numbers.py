# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = h = ListNode()
        overflow = 0
        while l1 or l2 or overflow:
            a = b = 0
            if l1:
                a = l1.val
                l1 = l1.next
            if l2:
                b = l2.val
                l2 = l2.next
            overflow, val = divmod(a + b + overflow,10)
            h.next = ListNode(val)
            h = h.next
        return head.next
