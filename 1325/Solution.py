```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if not root:
            return None
        res=[]
        def helper(root):
            if not root:
                return None
            root.left=helper(root.left)
            root.right=helper(root.right)
            
            if root.val==target:
                if root.left or root.right:
                    return root
                else:
                    return None
            
            return root
        
        return None if not helper(root) else root
```