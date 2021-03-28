# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            # 这一步找到root在inorder里的index 并且preorder pop掉第一个
            root_index = inorder.index(preorder.pop(0))
            new_node = TreeNode(inorder[root_index])
            new_node.left = self.buildTree(preorder, inorder[0:root_index])
            new_node.right = self.buildTree(preorder, inorder[root_index+1:])
            return new_node