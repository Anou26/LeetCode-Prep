class Solution:
    def goodNodes(self, root):
        def dfs(node, max_so_far):
            if not node:
                return 0  # Base case: empty node

            # Count current node as good if its value is >= the maximum seen so far
            count = 1 if node.val >= max_so_far else 0  

            # Update the maximum value for children
            new_max = max(max_so_far, node.val)  

            # Recursively check left and right subtrees
            count += dfs(node.left, new_max)  
            count += dfs(node.right, new_max)  

            return count
        
        # Start DFS from root with the root's value as the initial maximum
        return dfs(root, float('-inf'))  # Use negative infinity as the initial max value
