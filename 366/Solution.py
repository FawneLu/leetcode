```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        
        d=collections.defaultdict(list)
        def dfs(node,d):
            if not node:
                return 0
            left=dfs(node.left,d)
            right=dfs(node.right,d)
            level=1+max(left,right)
            d[level].append(node.val)
            
            return level
        
        dfs(root,d)
        res=[]
        for i in d:
            res.append(d[i])
        return res
```