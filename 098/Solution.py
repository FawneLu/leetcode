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
```python
class Solution:
     def isValidBST(self, root: TreeNode) -> bool:
            if not root:
                return True
            
            min_val=float('-inf')
            stack=[]
            
            while stack or root:
                while root:
                    stack.append(root)
                    root=root.left
                root=stack.pop()
                if root.val<=min_val:
                    return False
                min_val=root.val
                root=root.right
            return True
```