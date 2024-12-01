# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev=None
        self.mindiff=float('inf')
        def iot(node):
            if not node:
                return
            iot(node.left)
            if self.prev is not None:
                self.mindiff=min(self.mindiff,node.val-self.prev)
            self.prev=node.val
            iot(node.right)
        iot(root)
        return self.mindiff