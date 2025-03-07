"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
#Interleaving method
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        #First pass: Create new nodes and store mapping
        old_to_new = {}
        current = head
        while current:
            #Create a new node with the same value
            old_to_new[current] = Node(current.val)
            current = current.next

        #Second pass: Assign next and random pointers
        current = head
        while current:
            #set the next pointer
            if current.next:
                old_to_new[current].next = old_to_new[current.next]
            #set the random pointer
            if current.random:
                old_to_new[current].random = old_to_new[current.random]
            current = current.next
        #return the head of the copied list
        return old_to_new[head]


        