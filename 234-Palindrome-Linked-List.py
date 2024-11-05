class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Edge case: If the list is empty or has only one node
        if not head or not head.next:
            return True
        
        # Step 1: Find the midpoint of the linked list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the linked list
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        # Step 3: Compare the first half and the reversed second half
        left, right = head, prev  # 'right' points to the head of the reversed second half
        while right:  # No need to compare the entire left half if right is fully traversed
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True

        