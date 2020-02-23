```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            self.res=min(self.res,root.val-self.prev)
            self.prev=root.val
            dfs(root.right)
            
        self.res=float("inf")
        self.prev=float("-inf")
        dfs(root)
        return self.res
        
    
    def minDiffInBST1(self, root: TreeNode) -> int:
        val=[]
        def dfs(root):
            if root:
                val.append(root.val)
                dfs(root.left)
                dfs(root.right)
        
        dfs(root)
        val=sorted(val)
        return min(val[i+1]-val[i] for i in range(len(val)-1))
            
```