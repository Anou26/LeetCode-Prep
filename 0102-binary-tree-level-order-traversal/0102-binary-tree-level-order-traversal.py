# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# initialize queue with root
# add the left and right children across each individual level to the queue
# Edge Cases to consider:
# 1. Empty tree -> return []
# 2. Single Node -> return root
# 3. Greater than one node tree -> BFS
# Number of Nodes in the Tree cannot exceed [0, 2000]

from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result

        queue = deque([root]) #Initialize queue with root

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level)

        return result


        