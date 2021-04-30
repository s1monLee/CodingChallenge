# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if root:
                yield from dfs(root.left)
                yield root.val
                yield from dfs(root.right)
        #listOfObj = sorted(listOfObj, key = operator.attrgetter("val"))
        h = head = TreeNode(None)
        for i in dfs(root):
            head.right = TreeNode(i)
            head = head.right
        return h.right
