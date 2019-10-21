```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        tmp=0
        def helper(root):
            nonlocal tmp
            if not root:
                return 
            helper(root.right)
            tmp+=root.val
            root.val=tmp
            helper(root.left)
        
        helper(root)
        return root
```