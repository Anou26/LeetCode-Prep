# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        if not root:
            return False

        if self.isIdentical(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,subRoot)

    def isIdentical(self, p: Optional[TreeNode], q: Optional[TreeNode])->bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        return (p.val == q.val and self.isIdentical(p.left, q.left) and self.isIdentical(p.right, q.right))
        