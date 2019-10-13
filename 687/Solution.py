```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        longpath=0
        def maxdepth(root):
            nonlocal longpath
            
            if not root:
                return 0
            
            left=maxdepth(root.left)
            right=maxdepth(root.right)
            
            left=left+1 if root.left and root.val==root.left.val else 0
            right=right+1 if root.right and root.val==root.right.val else 0
            
            longpath=max(longpath,left+right)
            
            return max(left,right)
        
        maxdepth(root)
        
        return longpath
            
```