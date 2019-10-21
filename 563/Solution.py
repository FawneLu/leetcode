```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        res=0
        
        def helper(root):
            nonlocal res
            if not root:
                return 0
            
            left=helper(root.left)
            right=helper(root.right)
            
            res=res+abs(left-right)
            
            return left+right+root.val
        
        helper(root)
        return res
```