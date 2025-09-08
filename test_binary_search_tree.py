"""
Test cases for Binary Search Tree implementation

This file contains comprehensive test cases to verify the correctness
of the BST implementation.
"""

# Import the BST implementation
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import from the main file
exec(open('binary-search-tree.py').read())

def test_empty_bst():
    """Test operations on empty BST."""
    print("=== Testing Empty BST ===")
    bst = BinarySearchTree()
    
    assert bst.is_empty() == True
    assert bst.size() == 0
    assert bst.height() == -1
    assert bst.find_min() is None
    assert bst.find_max() is None
    assert bst.search(5) == False
    assert bst.inorder_traversal() == []
    assert bst.is_valid_bst() == True
    
    print("✓ All empty BST tests passed")

def test_single_node_bst():
    """Test operations on BST with single node."""
    print("\n=== Testing Single Node BST ===")
    bst = BinarySearchTree()
    bst.insert(42)
    
    assert bst.is_empty() == False
    assert bst.size() == 1
    assert bst.height() == 0
    assert bst.find_min() == 42
    assert bst.find_max() == 42
    assert bst.search(42) == True
    assert bst.search(43) == False
    assert bst.inorder_traversal() == [42]
    assert bst.is_valid_bst() == True
    
    print("✓ All single node BST tests passed")

def test_balanced_bst():
    """Test operations on balanced BST."""
    print("\n=== Testing Balanced BST ===")
    bst = BinarySearchTree()
    values = [50, 25, 75, 10, 30, 60, 80]
    
    for val in values:
        bst.insert(val)
    
    assert bst.size() == 7
    assert bst.height() == 2
    assert bst.find_min() == 10
    assert bst.find_max() == 80
    assert bst.inorder_traversal() == [10, 25, 30, 50, 60, 75, 80]
    assert bst.preorder_traversal() == [50, 25, 10, 30, 75, 60, 80]
    assert bst.is_valid_bst() == True
    
    print("✓ All balanced BST tests passed")

def test_skewed_bst():
    """Test operations on skewed (degenerate) BST."""
    print("\n=== Testing Skewed BST ===")
    bst = BinarySearchTree()
    values = [1, 2, 3, 4, 5]  # Right skewed
    
    for val in values:
        bst.insert(val)
    
    assert bst.size() == 5
    assert bst.height() == 4
    assert bst.find_min() == 1
    assert bst.find_max() == 5
    assert bst.inorder_traversal() == [1, 2, 3, 4, 5]
    assert bst.is_valid_bst() == True
    
    print("✓ All skewed BST tests passed")

def test_deletion_cases():
    """Test different deletion scenarios."""
    print("\n=== Testing Deletion Cases ===")
    
    # Test deleting leaf node
    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80]
    for val in values:
        bst.insert(val)
    
    bst.delete(20)  # Delete leaf
    assert 20 not in bst.inorder_traversal()
    assert bst.is_valid_bst() == True
    
    # Test deleting node with one child
    bst.delete(30)  # Delete node with one child (40)
    assert 30 not in bst.inorder_traversal()
    assert bst.is_valid_bst() == True
    
    # Test deleting node with two children
    bst.delete(50)  # Delete root with two children
    assert 50 not in bst.inorder_traversal()
    assert bst.is_valid_bst() == True
    
    # Test deleting non-existent node
    original_size = bst.size()
    bst.delete(999)
    assert bst.size() == original_size
    
    print("✓ All deletion tests passed")

def test_duplicate_insertion():
    """Test inserting duplicate values."""
    print("\n=== Testing Duplicate Insertion ===")
    bst = BinarySearchTree()
    
    bst.insert(50)
    bst.insert(50)  # Duplicate
    bst.insert(30)
    bst.insert(30)  # Duplicate
    
    # BST should not contain duplicates
    assert bst.size() == 2
    assert bst.inorder_traversal() == [30, 50]
    
    print("✓ All duplicate insertion tests passed")

def test_edge_cases():
    """Test various edge cases."""
    print("\n=== Testing Edge Cases ===")
    
    # Test with negative numbers
    bst = BinarySearchTree()
    values = [-50, -30, -70, 0, 25]
    for val in values:
        bst.insert(val)
    
    assert bst.find_min() == -70
    assert bst.find_max() == 25
    assert bst.inorder_traversal() == [-70, -50, -30, 0, 25]
    assert bst.is_valid_bst() == True
    
    # Test deleting from single node tree
    single_bst = BinarySearchTree()
    single_bst.insert(100)
    single_bst.delete(100)
    assert single_bst.is_empty() == True
    
    print("✓ All edge case tests passed")

def run_all_tests():
    """Run all test cases."""
    print("Running Binary Search Tree Tests...\n")
    
    try:
        test_empty_bst()
        test_single_node_bst()
        test_balanced_bst()
        test_skewed_bst()
        test_deletion_cases()
        test_duplicate_insertion()
        test_edge_cases()
        
        print("\n🎉 All tests passed successfully!")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")

if __name__ == "__main__":
    run_all_tests()