# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n==0:
            return []
        def build(low,high):
            trees=[]
            if low>high:
                return[None]
            for root_val in range(low,high+1):
                left_t=build(low,root_val-1)
                right_t=build(root_val+1,high)
                for left in left_t:
                    for right in right_t:
                        root=TreeNode(root_val)
                        root.left=left
                        root.right=right
                        trees.append(root)
            return trees
        return build(1,n)
        

        