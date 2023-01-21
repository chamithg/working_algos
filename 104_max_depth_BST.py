# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        levels =[]

        if not root:return 0

        def dfs(root,level):
            if not root:
                return
            if level not in levels:
                levels.append(level)
            dfs(root.left, level +1)
            dfs(root.right, level +1)
        
        
        dfs(root,1)
        return levels[-1]      
