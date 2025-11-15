"""
Binary Search Tree Implementation

A comprehensive implementation of a Binary Search Tree with all fundamental operations.
This implementation includes:
- TreeNode class for individual nodes
- BinarySearchTree class with core operations
- Insert, search, delete operations
- Traversal methods (inorder, preorder, postorder)
- Utility methods (find min/max, validate BST, height calculation)
"""

class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinarySearchTree:
    """
    Binary Search Tree implementation with comprehensive operations.
    """
    
    def __init__(self):
        """Initialize an empty BST."""
        self.root = None
    
    def insert(self, val):
        """
        Insert a value into the BST.
        
        Args:
            val: The value to insert
        """
        self.root = self._insert_recursive(self.root, val)
    
    def _insert_recursive(self, node, val):
        """
        Recursive helper method for insertion.
        
        Args:
            node: Current node
            val: Value to insert
            
        Returns:
            TreeNode: The updated node
        """
        if node is None:
            return TreeNode(val)
        
        if val < node.val:
            node.left = self._insert_recursive(node.left, val)
        elif val > node.val:
            node.right = self._insert_recursive(node.right, val)
        # If val == node.val, we don't insert duplicates
        
        return node
    
    def search(self, val):
        """
        Search for a value in the BST.
        
        Args:
            val: The value to search for
            
        Returns:
            bool: True if value exists, False otherwise
        """
        return self._search_recursive(self.root, val)
    
    def _search_recursive(self, node, val):
        """
        Recursive helper method for searching.
        
        Args:
            node: Current node
            val: Value to search for
            
        Returns:
            bool: True if found, False otherwise
        """
        if node is None:
            return False
        
        if val == node.val:
            return True
        elif val < node.val:
            return self._search_recursive(node.left, val)
        else:
            return self._search_recursive(node.right, val)
    
    def delete(self, val):
        """
        Delete a value from the BST.
        
        Args:
            val: The value to delete
        """
        self.root = self._delete_recursive(self.root, val)
    
    def _delete_recursive(self, node, val):
        """
        Recursive helper method for deletion.
        
        Args:
            node: Current node
            val: Value to delete
            
        Returns:
            TreeNode: The updated node
        """
        if node is None:
            return node
        
        if val < node.val:
            node.left = self._delete_recursive(node.left, val)
        elif val > node.val:
            node.right = self._delete_recursive(node.right, val)
        else:
            # Node to be deleted found
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Node with two children
            # Find the inorder successor (smallest in the right subtree)
            min_node = self._find_min_node(node.right)
            node.val = min_node.val
            node.right = self._delete_recursive(node.right, min_node.val)
        
        return node
    
    def _find_min_node(self, node):
        """
        Find the node with minimum value in a subtree.
        
        Args:
            node: Root of the subtree
            
        Returns:
            TreeNode: Node with minimum value
        """
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def find_min(self):
        """
        Find the minimum value in the BST.
        
        Returns:
            int: Minimum value, or None if tree is empty
        """
        if self.root is None:
            return None
        node = self._find_min_node(self.root)
        return node.val
    
    def find_max(self):
        """
        Find the maximum value in the BST.
        
        Returns:
            int: Maximum value, or None if tree is empty
        """
        if self.root is None:
            return None
        
        current = self.root
        while current.right is not None:
            current = current.right
        return current.val
    
    def inorder_traversal(self):
        """
        Perform inorder traversal of the BST.
        
        Returns:
            list: Values in inorder (sorted order for BST)
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        """
        Recursive helper for inorder traversal.
        
        Args:
            node: Current node
            result: List to store values
        """
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.val)
            self._inorder_recursive(node.right, result)
    
    def preorder_traversal(self):
        """
        Perform preorder traversal of the BST.
        
        Returns:
            list: Values in preorder
        """
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        """
        Recursive helper for preorder traversal.
        
        Args:
            node: Current node
            result: List to store values
        """
        if node:
            result.append(node.val)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def postorder_traversal(self):
        """
        Perform postorder traversal of the BST.
        
        Returns:
            list: Values in postorder
        """
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node, result):
        """
        Recursive helper for postorder traversal.
        
        Args:
            node: Current node
            result: List to store values
        """
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.val)
    
    def height(self):
        """
        Calculate the height of the BST.
        
        Returns:
            int: Height of the tree (0 for single node, -1 for empty tree)
        """
        return self._height_recursive(self.root)
    
    def _height_recursive(self, node):
        """
        Recursive helper for height calculation.
        
        Args:
            node: Current node
            
        Returns:
            int: Height of the subtree
        """
        if node is None:
            return -1
        
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        
        return max(left_height, right_height) + 1
    
    def is_valid_bst(self):
        """
        Validate if the tree is a valid BST.
        
        Returns:
            bool: True if valid BST, False otherwise
        """
        return self._is_valid_bst_recursive(self.root, float('-inf'), float('inf'))
    
    def _is_valid_bst_recursive(self, node, min_val, max_val):
        """
        Recursive helper for BST validation.
        
        Args:
            node: Current node
            min_val: Minimum allowed value
            max_val: Maximum allowed value
            
        Returns:
            bool: True if valid BST, False otherwise
        """
        if node is None:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return (self._is_valid_bst_recursive(node.left, min_val, node.val) and
                self._is_valid_bst_recursive(node.right, node.val, max_val))
    
    def size(self):
        """
        Get the number of nodes in the BST.
        
        Returns:
            int: Number of nodes
        """
        return self._size_recursive(self.root)
    
    def _size_recursive(self, node):
        """
        Recursive helper for size calculation.
        
        Args:
            node: Current node
            
        Returns:
            int: Number of nodes in subtree
        """
        if node is None:
            return 0
        
        return 1 + self._size_recursive(node.left) + self._size_recursive(node.right)
    
    def is_empty(self):
        """
        Check if the BST is empty.
        
        Returns:
            bool: True if empty, False otherwise
        """
        return self.root is None
    
    def display(self):
        """
        Display the BST structure (simple representation).
        """
        if self.root is None:
            print("Empty BST")
            return
        
        print("BST Structure (Inorder):", self.inorder_traversal())
        print("BST Structure (Preorder):", self.preorder_traversal())
        print("Height:", self.height())
        print("Size:", self.size())
        print("Min value:", self.find_min())
        print("Max value:", self.find_max())
        print("Is valid BST:", self.is_valid_bst())


# Example usage and testing
if __name__ == "__main__":
    # Create a new BST
    bst = BinarySearchTree()
    
    # Test insertion
    print("=== Testing BST Operations ===")
    values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]
    print(f"Inserting values: {values}")
    
    for val in values:
        bst.insert(val)
    
    # Display BST information
    print("\n=== BST Information ===")
    bst.display()
    
    # Test search operations
    print("\n=== Testing Search Operations ===")
    test_values = [25, 75, 50, 100]
    for val in test_values:
        found = bst.search(val)
        print(f"Search for {val}: {'Found' if found else 'Not found'}")
    
    # Test traversals
    print("\n=== Testing Traversals ===")
    print("Inorder (sorted):", bst.inorder_traversal())
    print("Preorder:", bst.preorder_traversal())
    print("Postorder:", bst.postorder_traversal())
    
    # Test deletion
    print("\n=== Testing Deletion ===")
    delete_values = [20, 30, 50]
    for val in delete_values:
        print(f"Deleting {val}")
        bst.delete(val)
        print("Inorder after deletion:", bst.inorder_traversal())
    
    # Final state
    print("\n=== Final BST State ===")
    bst.display()