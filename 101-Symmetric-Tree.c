bool isMirror(struct TreeNode* left, struct TreeNode* right) {
    // Both nodes are NULL, they are mirrors
    if (left == NULL && right == NULL) {
        return true;
    }
    
    // One of the nodes is NULL, they are not mirrors
    if (left == NULL || right == NULL) {
        return false;
    }
    
    // Check if current nodes are equal and recurse on children
    return (left->val == right->val) &&
           isMirror(left->left, right->right) &&
           isMirror(left->right, right->left);
}

bool isSymmetric(struct TreeNode* root) {
    // An empty tree is symmetric
    if (root == NULL) {
        return true;
    }
    
    // Check if left and right subtrees are mirrors of each other
    return isMirror(root->left, root->right);
}
