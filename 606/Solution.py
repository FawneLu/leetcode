```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ""
        def preorder(t):
            if not t:
                return ""
            if not t.left and not t.right:
                return str(t.val)
            elif not t.right:
                return str(t.val)+"("+preorder(t.left)+")"
            else:
                return str(t.val)+"("+preorder(t.left)+")"+"("+preorder(t.right)+")"
            
        res=preorder(t)
        return res
```