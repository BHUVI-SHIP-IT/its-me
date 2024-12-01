bool isSameTree(struct TreeNode* p, struct TreeNode* q) {
    // Both nodes are NULL, trees are the same
    if (p == NULL && q == NULL) {
        return true;
    }
    
    // One of the nodes is NULL, trees are not the same
    if (p == NULL || q == NULL) {
        return false;
    }
    
    // Check the value of the current nodes and recurse on left and right children
    return (p->val == q->val) &&
           isSameTree(p->left, q->left) &&
           isSameTree(p->right, q->right);
}
