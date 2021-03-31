# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        return self.helper(root.left, root.right)
    
    def helper(self, left, right):
        #两个node都越出边界
        if not left and not right: return True
        #其中一个跃出边界-> 不对称
        if (not left and right) or (not right and left): return False
        #注意left right交替
        return left.val == right.val and self.helper(left.right, right.left) and self.helper(left.left, right.right)