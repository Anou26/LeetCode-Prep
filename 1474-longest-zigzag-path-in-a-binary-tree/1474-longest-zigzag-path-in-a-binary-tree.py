# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node, direction, length):
            if not node:
                return
            
            # Update the maximum ZigZag length found
            self.max_length = max(self.max_length, length)
            
            # If the current direction is left, go right, and vice versa
            if direction == 'left':
                dfs(node.left, 'right', length + 1)  # Continue left path
                dfs(node.right, 'left', 1)  # Switch to right path, reset length
            else:  # direction == 'right'
                dfs(node.right, 'left', length + 1)  # Continue right path
                dfs(node.left, 'right', 1)  # Switch to left path, reset length

        # Initialize max_length to track the maximum ZigZag path
        self.max_length = 0

        # Start DFS from the left and right children of the root with initial length 1
        if root:
            dfs(root.left, 'right', 1)
            dfs(root.right, 'left', 1)

        return self.max_length
