# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
       # Dummy node initialization
        dummy = ListNode(0)
        dummy.next = head
        groupPrev = dummy
        
        while True:
            # Check if there are k nodes remaining in the list
            kth = self.getKthNode(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next
            
            # Reverse the group: 
            # starting at groupPrev.next up to kth.
            prev, curr = kth.next, groupPrev.next
            
            # Reverse the nodes in the current group
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # After reversal, groupPrev.next is the tail of the reversed group.
            temp = groupPrev.next  # This is the tail after reversal.
            groupPrev.next = kth  # kth becomes the new head of this group.
            groupPrev = temp      # Move groupPrev to the end of the reversed group.
        
        return dummy.next
    
    def getKthNode(self, curr: ListNode, k: int) -> ListNode:
        # Helper function to get the kth node from the current position.
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr