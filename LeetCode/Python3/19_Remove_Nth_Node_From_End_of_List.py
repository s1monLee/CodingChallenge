# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next == None:
            head = None
            return head
        h = head
        arr = [ListNode()]*30
        i = 0
        while h:
            arr[i] = h
            h = h.next
            i += 1
        if i == n:
            head = arr[1]
        elif n == 1:
            arr[i-2].next = None
        else:
            arr[i-n-1].next = arr[i-n+1]
        
        return head
"""
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
