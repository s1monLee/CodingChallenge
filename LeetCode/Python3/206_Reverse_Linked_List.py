# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        stack = []
        a = head
        while a:
            stack.append(a.val)
            a = a.next
        b = head
        while head:
            head.val = stack.pop()
            head = head.next
        return b
