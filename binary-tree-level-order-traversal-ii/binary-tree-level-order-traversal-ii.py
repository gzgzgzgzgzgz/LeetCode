# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue = [root]
        res = []
        while queue:
            l = []
            res.append([i.val for i in queue])
            for j in queue:
                if j.left:
                    l.append(j.left)
                if j.right:
                    l.append(j.right)
            queue = l
        return res[::-1]