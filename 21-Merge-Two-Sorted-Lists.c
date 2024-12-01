



struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    // Create a dummy node to serve as the starting point of the merged list
    struct ListNode dummy;
    struct ListNode* current = &dummy;  // Pointer to build the merged list
    dummy.next = NULL;

    // Traverse both lists until one is exhausted
    while (list1 != NULL && list2 != NULL) {
        if (list1->val <= list2->val) {
            current->next = list1;  // Append list1's node
            list1 = list1->next;    // Move to the next node in list1
        } else {
            current->next = list2;  // Append list2's node
            list2 = list2->next;    // Move to the next node in list2
        }
        current = current->next;  // Move the current pointer forward
    }

    // If one of the lists still has remaining nodes, append them to the result
    if (list1 != NULL) {
        current->next = list1;
    } else if (list2 != NULL) {
        current->next = list2;
    }

    // Return the merged list starting from the next node of the dummy
    return dummy.next;
}
