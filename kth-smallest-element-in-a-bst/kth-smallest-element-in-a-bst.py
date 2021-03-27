# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root):
        if root == None: return;
        self.inorder(root.left)
        self.inorder_list.append(root)
        self.inorder(root.right)
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.inorder_list = []
        self.inorder(root)
        return self.inorder_list[k - 1].val