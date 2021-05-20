# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = [[]for _ in range(2000)]
        self.i_max = 0
        def rec(root: TreeNode, i:int):
            self.i_max = max(i, self.i_max)
            if not root:
                return
            ans[i].append(root.val)
            rec(root.left, i+1)
            rec(root.right, i+1)
        rec(root, 0)
        
        return ans[:self.i_max]
