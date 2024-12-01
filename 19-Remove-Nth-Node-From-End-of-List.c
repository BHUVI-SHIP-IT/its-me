

// Function to remove the nth node from the end of the list
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    struct ListNode dummy; // Create a dummy node to handle edge cases
    dummy.next = head;
    struct ListNode* slow = &dummy;
    struct ListNode* fast = &dummy;

    // Move fast ahead by n + 1 nodes
    for (int i = 0; i <= n; i++) {
        fast = fast->next;
    }

    // Move both pointers until fast reaches the end
    while (fast != NULL) {
        slow = slow->next;
        fast = fast->next;
    }

    // Now slow is just before the node to be removed
    struct ListNode* toDelete = slow->next;
    slow->next = slow->next->next; // Remove the nth node

    free(toDelete); // Free the memory of the removed node
    return dummy.next; // Return the head of the modified list
}

// Helper function to create a new node
struct ListNode* createNode(int val) {
    struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
    newNode->val = val;
    newNode->next = NULL;
    return newNode;
}

// Helper function to print the linked list
void printList(struct ListNode* head) {
    while (head != NULL) {
        printf(\%d -> \, head->val);
        head = head->next;
    }
    printf(\NULL\
\);
}


