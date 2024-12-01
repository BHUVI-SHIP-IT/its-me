

bool hasCycle(struct ListNode *head) {
    // Initialize slow and fast pointers
    struct ListNode *slow = head;
    struct ListNode *fast = head;
    
    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;          // Move slow pointer one step
        fast = fast->next->next;    // Move fast pointer two steps
        
        // If slow and fast meet, there is a cycle
        if (slow == fast) {
            return true;
        }
    }
    
    // If we reach here, there is no cycle
    return false;
}
