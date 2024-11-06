

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []  # List to store all the paths from root to leaf

        def dfs(node, current_path):
            if node:
                # Append the current node's value to the path
                current_path += str(node.val)
                
                # If the node is a leaf, add the complete path to paths
                if not node.left and not node.right:
                    paths.append(current_path)
                else:
                    # Continue the path with \->\ for further nodes
                    current_path += \->\
                    dfs(node.left, current_path)
                    dfs(node.right, current_path)

        # Start DFS from the root with an empty path
        dfs(root, \\)
        return paths


        
