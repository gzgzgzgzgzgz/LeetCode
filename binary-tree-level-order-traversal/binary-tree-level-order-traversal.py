# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return root
        queue = []
        queue.append(root)
        r = []
        while queue:
            r.append([i.val for i in queue])
            #存储当前level的所有节点
            l = []
            for node in queue:
                if node.left:
                    l.append(node.left)
                if node.right:
                    l.append(node.right)
            #更新queue
            queue = l
        return r
            
            
            
        