```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        sum_ = 0 
        res = False
        
        def helper(root,sum_):
            nonlocal res
            if not root: return 
            
            if not root.left and not root.right:
                sum_ += root.val
                if sum_ == sum:
                    res = True
                
            helper(root.left, sum_+ root.val)
            helper(root.right, sum_ + root.val)
        
        helper(root,sum_)
        
        return res
```
```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        sum_ = 0 
        res = False
        
        def helper(root,sum_):
            nonlocal res
            if not root: return 
        
            sum_+=root.val
            if not root.left and not root.right:
                if sum_ == sum:
                    res = True
                
            helper(root.left, sum_)
            helper(root.right, sum_)
        
        helper(root,sum_)
        
        return res
```