

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Helper function to reverse a segment of the list
        def reverseLinkedList(head: ListNode, k: int) -> ListNode:
            prev, curr = None, head
            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev

        # Dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy
        
        while True:
            # Find the k-th node from the current position
            kth_node = prev_group
            for _ in range(k):
                kth_node = kth_node.next
                if not kth_node:
                    return dummy.next
            
            # Reverse the next k nodes
            group_head = prev_group.next
            next_group = kth_node.next
            # Disconnect the current group
            kth_node.next = None
            
            # Reverse the current group
            new_group_head = reverseLinkedList(group_head, k)
            
            # Connect the reversed group to the previous part of the list
            prev_group.next = new_group_head
            group_head.next = next_group
            
            # Move prev_group to the end of the reversed group
            prev_group = group_head

        