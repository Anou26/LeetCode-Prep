# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# dfs:
# initialize our max diameter = 0
# base case, empty list or no node -> return 0
# use recursion to find height of left and right subtrees
# update diameter if current path is longer
# return the height of the current subtree

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def dfs(node):
            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            self.diameter = max(self.diameter, left_height+right_height)

            return max(left_height, right_height) + 1

        dfs(root)
        return self.diameter
           

