```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def helper(root, low=float('-inf'), high=float('inf')):
            if not root:
                return True
            
            if root.val<=low or root.val>=high:
                return False
            
            if not helper( root.left, low, root.val):
                return False
            
            if not helper( root.right, root.val, high):
                return False
            
            return True
```