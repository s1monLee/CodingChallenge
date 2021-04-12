# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        l = list1
        while b != 0:
            l = l.next
            b -= 1
        ll = list2
        while ll.next != None:
            ll = ll.next
        ll.next = l.next 
        l = list1
        while a-1 != 0:
            l = l.next
            a -= 1
        l.next = list2
        return list1
            
