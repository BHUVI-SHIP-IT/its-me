#include <stdbool.h>

// Definition for a binary tree node.


bool hasPathSum(struct TreeNode* root, int targetSum) {
    // Base case: if the node is NULL, there's no path
    if (root == NULL) {
        return false;
    }
    
    // Check if we are at a leaf node
    if (root->left == NULL && root->right == NULL) {
        // If it's a leaf, check if the current value equals the targetSum
        return root->val == targetSum;
    }
    
    // Subtract the current node's value from targetSum and recurse on children
    targetSum -= root->val;
    
    return hasPathSum(root->left, targetSum) || hasPathSum(root->right, targetSum);
}
