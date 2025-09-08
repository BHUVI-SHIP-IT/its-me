"""
Binary Search Tree - Core Implementation

A clean, focused implementation of Binary Search Tree with essential operations.
Follows the pattern of other algorithm implementations in this repository.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        """Insert a value into the BST."""
        self.root = self._insert(self.root, val)
    
    def _insert(self, node, val):
        if not node:
            return TreeNode(val)
        
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        
        return node
    
    def search(self, val):
        """Search for a value in the BST."""
        return self._search(self.root, val)
    
    def _search(self, node, val):
        if not node or node.val == val:
            return node is not None
        
        if val < node.val:
            return self._search(node.left, val)
        return self._search(node.right, val)
    
    def delete(self, val):
        """Delete a value from the BST."""
        self.root = self._delete(self.root, val)
    
    def _delete(self, node, val):
        if not node:
            return node
        
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            # Node to delete found
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            # Node with two children - find inorder successor
            temp = self._find_min(node.right)
            node.val = temp.val
            node.right = self._delete(node.right, temp.val)
        
        return node
    
    def _find_min(self, node):
        """Find minimum value node in subtree."""
        while node.left:
            node = node.left
        return node
    
    def inorder(self):
        """Return inorder traversal (sorted order)."""
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.val)
            self._inorder(node.right, result)
    
    def preorder(self):
        """Return preorder traversal."""
        result = []
        self._preorder(self.root, result)
        return result
    
    def _preorder(self, node, result):
        if node:
            result.append(node.val)
            self._preorder(node.left, result)
            self._preorder(node.right, result)
    
    def postorder(self):
        """Return postorder traversal."""
        result = []
        self._postorder(self.root, result)
        return result
    
    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.val)

# Example usage
if __name__ == "__main__":
    bst = BST()
    
    # Insert values
    values = [50, 30, 70, 20, 40, 60, 80]
    for val in values:
        bst.insert(val)
    
    print("Inorder traversal:", bst.inorder())
    print("Search 40:", bst.search(40))
    print("Search 90:", bst.search(90))
    
    # Delete a value
    bst.delete(30)
    print("After deleting 30:", bst.inorder())