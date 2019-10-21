```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        
        return self.DFS(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
    
    def DFS(self,s,t):
            if not s and not t:
                return True
            elif not s or not t:
                return False
            
            return s.val==t.val and self.DFS(s.left,t.left) and self.DFS(s.right,t.right)
```