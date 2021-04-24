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
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        self.ans = False
        def rec2(root, head):
            if not head: return
            if not root: return
        
            if head.val == root.val:
                if not head.next:
                    self.ans = True
                rec2(root.left, head.next)
                rec2(root.right, head.next)
            
        def rec(root, head):
            if not root: return 
            
            if head.val == root.val:
                rec2(root, head)
                    
            rec(root.left, head)
            rec(root.right, head)
            
        rec(root, head)
        return self.ans
