# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        first = slow = fast = head
        for _ in range(1,k):
            fast = fast.next
        first = fast
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.val, first.val = first.val, slow.val
        return head
