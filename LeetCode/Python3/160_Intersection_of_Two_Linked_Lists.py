# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ListNode.marker = 0
        while headA:
            headA.marker = 1
            headA = headA.next
        while headB:
            if headB.marker == 1:
                return headB
            headB = headB.next
        delattr(ListNode, "marker")
        return headA
"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        hA = headA
        hB = headB
        
        while hA != hB:
            hA = headB if not hA else hA.next
            hB = headA if not hB else hB.next
        
        return hA
