```python3
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.depth=0
        
        if not root:
            return self.depth
        
        left=self.maxDepth(root.left)
        right=self.maxDepth(root.right)
        
        self.depth=max(self.depth,max(left,right)+1)
        
        return self.depth
```
```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        
        depth=0
        
        def helper(root):
            nonlocal depth
        
            if not root:
                return 0
            
            left=helper(root.left)
            right=helper(root.right)

            if root.left:
                left+=1
            if root.right:
                right+=1
                
            depth=max(left,right)

            return depth
        
        helper(root)
        return depth+1
```