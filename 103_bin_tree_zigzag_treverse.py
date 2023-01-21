# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        nodeMap = []

        def dfs(root,level):
            if not root:return
            if len(nodeMap) <= level-1:
                nodeMap.append([root.val])
            else:
                nodeMap[level-1].append(root.val)

            dfs(root.left,level+1)
            dfs(root.right,level+1) 

        dfs(root,1)
        for i,v in enumerate(nodeMap):
            if i%2 ==1:
                for j in range(len(v)//2):
                    v[j],v[len(v)-1-j] = v[len(v)-1-j],v[j]
        return nodeMap
