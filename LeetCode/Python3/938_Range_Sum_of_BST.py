# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.ans = 0
        def rec(root):
            if not root: return
            if low <= root.val <= high: self.ans += root.val
            rec(root.left)
            rec(root.right)
        rec(root)
        return self.ans
