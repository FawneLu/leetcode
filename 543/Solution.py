```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        res=0
        
        def helper(root):
            nonlocal res
            
            if not root:
                return 0
            
            left=helper(root.left)
            right=helper(root.right)
            
            if root.left:
                left+=1
            if root.right:
                right+=1
            
            res=max(left+right,res)
            
            return max(left,right)
        
        helper(root)
        
        return res
```
