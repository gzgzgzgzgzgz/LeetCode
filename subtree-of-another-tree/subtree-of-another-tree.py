# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s or not t:
            return False
        def dfs(root_a, root_b):
            if not root_b and not root_a: return True
            if not root_b or not root_a: return False
            if root_a.val != root_b.val: return False
            return root_a.val == root_b.val and dfs(root_a.left, root_b.left) and dfs(root_a.right, root_b.right)
        return dfs(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
