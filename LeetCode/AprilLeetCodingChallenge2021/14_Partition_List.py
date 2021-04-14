# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head or head.next == None: return head
        head2 = tail2 = None
        head3 = tail3 = None
        h = head
        while h:    
            if h.val < x:
                if tail2:
                    tail2.next = ListNode(h.val)
                    tail2 = tail2.next
                else:
                    head2 = tail2 = ListNode(h.val)
            if h.val >= x:
                if tail3:
                    tail3.next = ListNode(h.val)
                    tail3 = tail3.next
                else:
                    head3 = tail3 = ListNode(h.val)
            h = h.next
        if not head2 or not head3: return head
        tail2.next = head3
        return head2
                
