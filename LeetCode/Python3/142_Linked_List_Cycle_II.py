# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        def is_cycle(head):
            fast = slow = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return True, slow
            return False, slow
        loop, fast = is_cycle(head)
        if loop:
            while head != fast:
                head = head.next
                fast = fast.next
            return fast
        return None
