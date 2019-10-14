```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        sum=0
        
        cur=TreeNode(None)
        
        def helper(root):
            nonlocal sum
            
            if not root:
                return 0
            if root.left:
                if not root.left.left and not root.left.right:
                    sum+=root.left.val
                
            helper(root.left)
            helper(root.right)
            
            return sum
        
        helper(root)
        return sum
```