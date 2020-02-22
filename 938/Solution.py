```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        res=0
        if not root:
            return res
        if root.val>=L and root.val<=R:
            res+=root.val
        if root.val>L:
            res+= self.rangeSumBST(root.left,L,R)
        if root.val<R:
            res+= self.rangeSumBST(root.right,L,R)
        
        return res
        
    
    
    
    
    def rangeSumBST1(self, root: TreeNode, L: int, R: int) -> int:
        self.res=0
        
        def dfs(root):
            if not root:
                return
            if root.val>=L and root.val<=R:
                self.res+=root.val
            if root.val>L:
                dfs(root.left)
            if root.val<R:
                dfs(root.right)
                
        
        dfs(root)
        return self.res
```