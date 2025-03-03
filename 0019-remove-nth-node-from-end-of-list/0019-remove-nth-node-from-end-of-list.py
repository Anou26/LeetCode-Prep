class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)  # Dummy node before head to handle edge cases
        fast = slow = dummy  # Both pointers start from the dummy node

        # Step 1: Move `fast` pointer `n+1` steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # Step 2: Move both `slow` and `fast` until `fast` reaches the end
        while fast:
            slow = slow.next
            fast = fast.next

        # Step 3: Remove the target node
        slow.next = slow.next.next

        return dummy.next  # Return the new head
