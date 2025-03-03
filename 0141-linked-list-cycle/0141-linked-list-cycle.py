class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head  # Moves one step at a time
        fast = head  # Moves two steps at a time

        while fast and fast.next:
            slow = slow.next  # Move slow one step
            fast = fast.next.next  # Move fast two steps

            if slow == fast:  # Cycle detected
                return True

        return False  # No cycle
