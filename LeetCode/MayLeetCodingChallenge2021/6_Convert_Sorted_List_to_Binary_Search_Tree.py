# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        l = []
        while head:
            l.append(head.val)
            head = head.next
            
        def createBST(l):
            if not l: return None
            mid = len(l)//2
            root = TreeNode(l[mid])
            root.left, root.right = createBST(l[:mid]), createBST(l[mid+1:])
            return root
        return createBST(l)
        
