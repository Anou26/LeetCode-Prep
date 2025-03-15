class Solution:
    def isValidBST(self, root):
        def dfs(node, min_val, max_val):
            if not node:
                return True  # Base case: empty tree is valid
            
            # Check if node violates BST property
            if not (min_val < node.val < max_val):
                return False

            # Recursively check left and right subtrees with updated ranges
            return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)

        # Start DFS with the full valid range (-inf, inf)
        return dfs(root, float('-inf'), float('inf'))
